import os
import dotenv
from dotenv.main import load_dotenv
import requests

load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.acc_id = os.getenv('tequila_id')
        self.acc_api = os.getenv('tequila_api')
        self.base_url = 'https://tequila-api.kiwi.com/v2'

    def search(self, fly_from: str, fly_to:str, date_from:str, date_to:str):
        search_url = f"{self.base_url}/search"
        t_head = {'apikey' : self.acc_api}
        t_params = {'fly_from' : fly_from, 'fly_to': fly_to, 'dateFrom' : date_from, 'dateTo': date_to, 'curr':'AUD',
        'max_stopovers':1}
        t_resp = requests.get(url=search_url, headers=t_head, params=t_params)
        t_resp.raise_for_status()
        data = t_resp.json()
        return data['data']