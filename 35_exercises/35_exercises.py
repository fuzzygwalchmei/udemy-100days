import requests
from requests import api
from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()

# Details for api.openweather.org
api_key=os.getenv('WEATHER_API')
city_name = 'Sydney'
cur_url = f'http://api.openweathermap.org/data/2.5/weather'
one_url = 'https://api.openweathermap.org/data/2.5/onecall'

# Lat and Long for Sydney
# LONG= 151.21
# LAT= -33.87

# Location Bern just because it was raining
LONG=7.447447
LAT=46.947975

# Twilio details
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
client = Client(account_sid, auth_token)


# fuction to send message via Twilio
def send_sms():
    message = client.messages.create(
                              body='Bad weather ahead, take an umbrella!',
                              from_='+12513104416',
                              to='+61409464473'
                          )
    print(message.status)

# Get weather via openweather api
cur_params = {'q': city_name, 'appid': api_key}
one_params = {'lat': LAT, 'lon': LONG, 'appid': api_key, 'exclude': 'minutely,daily,current,alerts'}

response = requests.get(url=one_url, params=one_params)
response.raise_for_status()
data = response.json()
umbrella = False

for hour in data['hourly'][:12]:
    if hour['weather'][0]['id'] < 700:
        umbrella = True

if umbrella:
    print('GOnna rain')
    # send_sms()
else:
    print('Not required')