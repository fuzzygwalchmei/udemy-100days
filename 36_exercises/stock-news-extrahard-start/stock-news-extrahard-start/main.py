from dotenv import load_dotenv
import os
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
articles = []
load_dotenv()


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
alpha_url = 'https://www.alphavantage.co/query'
alpha_params = {'function':'TIME_SERIES_DAILY',
                'symbol': STOCK,
                'apikey': os.getenv('alpha_api')}

a_response = requests.get(url=alpha_url, params = alpha_params)
a_response.raise_for_status()
a_data = a_response.json()['Time Series (Daily)']
a_dates = list(a_data.keys())

day_0 = a_data[a_dates[0]]['4. close']
day_1 = a_data[a_dates[1]]['4. close']
a_diff = float(day_0) - float(day_1)
a_perc = int((a_diff/float(day_1))*100)


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def get_news():
    news_url = "https://newsapi.org/v2/everything"
    news_params = {'country': 'us',
                'apiKey': os.getenv('news_api'),
                'q':COMPANY_NAME}

    n_response = requests.get(url=news_url, params=news_params)
    n_response.raise_for_status()
    n_data = n_response.json()['articles']
    return n_data[:3]

if a_perc >= 5:
    articles = get_news()

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
# Twilio details
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
client = Client(account_sid, auth_token)

# fuction to send message via Twilio
def send_sms(message):
    message = client.messages.create(
                            body=message,
                            from_='+12513104416',
                            to='+61409464473'
                        )
    print(message.status)

a_change = f"🔺{a_perc}%" if a_perc > 0 else f"🔻{a_perc * -1}%"
if len(articles) > 0:
    n_head = articles[0]['title']
    n_brief = articles[0]['description']
else:
    n_head = "No news articles found"
    n_brief = "No news articles found"

message = f"""
TSLA: {a_change}
Headline: {n_head}
Brief: {n_brief}
"""
print(message)

# send_sms(message=message)



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

