import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests_cache
import smtplib

load_dotenv()

USERNAME = os.getenv('email_user')
PASSWORD = os.getenv('email_token')

# Check price of item

def get_price():
    requests_cache.install_cache(cache_name='amazone_cache', backend='sqlite', expire_after=500)

    pot_url = 'https://www.amazon.com.au/Exploding-Kittens-Card-Game-Family-Friendly/dp/B0825N5Y7V/'

    headers = {'Accept-Language': 'en-AU,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}

    resp = requests.get(url=pot_url, headers=headers)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, 'html.parser')

    price = float(soup.find('span', id='priceblock_ourprice').getText().replace('$',''))

    return price


# Send email function
def send_email():
    with smtplib.SMTP('smtp.mail.yahoo.com') as connection:
        connection.starttls()

        connection.login(user=USERNAME, password=PASSWORD)
        connection.sendmail(
            from_addr=USERNAME,
            to_addrs='marc.falzon@gmail.com',
            msg=f'Subject: Exploding Kittens under $30!\n\nThis should appear in the body?'.encode('utf-8')
            )
        print('Email sent')
        

def check_price(price):
    if price < 30:
        send_email()

price = get_price()
check_price(price)
