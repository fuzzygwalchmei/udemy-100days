import dotenv
from dotenv.main import load_dotenv
import os
import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.token = os.getenv('sheety_token')
        self.header = {'Authorization': f'Bearer {self.token}'}
        self.base_url = os.getenv('sheety_url')

    def get_data(self):
        resp = requests.get(url = f"{self.base_url}prices", headers=self.header)
        resp.raise_for_status()
        return resp.json()

    def update_data(self, id:int, price:int):
        update_url = f"{self.base_url}prices/{id}"
        requests.put(url=update_url, headers=self.header, json={'price': {'lowestPrice':price}})

    def get_users(self):
        resp = requests.get(url=f"{self.base_url}users", headers=self.header)
        resp.raise_for_status()
        return resp.json()['users']

    def create_user(self, u_first:str, u_last:str, u_email:str):
        u_json = {'user':{"firstName": u_first, "lastName": u_last, "email": u_email}}
        resp = requests.post(url=f"{self.base_url}users", headers=self.header, json=u_json)
        resp.raise_for_status()