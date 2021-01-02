import os
from dotenv import load_dotenv
import requests
import datetime as dt



load_dotenv()

NUTR_APP = os.getenv('nutritionix_id')
NUTR_API = os.getenv('nutritionix_apikey')
SHEET_UN = os.getenv('sheety_un')
SHEET_PW = os.getenv('sheety_pw')
SHEET_TK = os.getenv('sheety_token')
SHEET_HEADER = {'Authorization': f'Bearer {SHEET_TK}'}
TIMEZONE = 'Australia/Sydney'

n_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
s_url = os.getenv('sheety_url')
n_header = {'x-app-id':NUTR_APP, 'x-app-key':NUTR_API, 'Content-Type':'application/json'}

query = input("What did you want to add?: ").lower()
time_now = dt.datetime.now()

params = {
"query":query,
"gender":"male",
"weight_kg":105.5,
"height_cm":180.64,
"age":42
}

response = requests.post(n_url, headers=n_header, json=params)
response.raise_for_status()
data = response.json()

# print(data)
for each in data['exercises']:
    #put data into sheety
    row_data = {'workout':{'date':time_now.strftime(format='%d/%m/%Y'), 'time':time_now.strftime(format='%H:%M:%S'),
    'exercise': each['name'], 'duration':  each['duration_min'], 'calories':each['nf_calories']}}

    # Using Username and Password
    # s_response = requests.post(url=s_url, json=row_data, auth=(SHEET_UN, SHEET_PW), )

    # Using Bearer Token
    print(SHEET_HEADER)
    s_response = requests.post(url=s_url, headers=SHEET_HEADER, json=row_data, )

    s_response.raise_for_status()
    print(s_response.text)
   