import requests
from dotenv import load_dotenv
import os
import datetime as dt

load_dotenv()

P_TOKEN = os.getenv('pixela_token') 
P_USER = os.getenv('pixela_username')

header = {'token': P_TOKEN, 'username': P_USER}

today = dt.datetime.today().strftime(format="%Y%m%d")

## Create user account
#
P_URL = "https://pixe.la/v1/users"
# user_params = {
#     "token" : "not my real token",
#     "username" : "fuzzygwalchmei",
#     "agreeTermsOfService" : "yes",
#     "notMinor" : "yes"
# }

# response = requests.get(url = P_URL, params=user_params)

# Create initial Graph

graph_url = f"{P_URL}/{P_USER}/graphs"
graph_header = {'X-USER-TOKEN' : P_TOKEN}
# graph_params = {
#     "id" : "testgraph01",
#     "name" : "Test Graph 01",
#     "unit" : "commit",
#     "type" : "int",
#     "color" : "shibafu",
#     "timezone" : "Australia/Sydney"
#     }

# graph_resp = requests.post(url=graph_url, headers=graph_header, json=graph_params)
# print(graph_resp.text)

# del_resp = requests.delete(url=f"{graph_url}/testgraph01", headers=graph_header)
# print(del_resp.text)

# Add a pixel


# add_params = {
#     "date" : today,
#     "quantity" : "7"
# }

# add_resp = requests.post(url=f"{graph_url}/testgraph01", headers=graph_header, json=add_params)

# print(add_resp.text)

# Update graph

put_url = f"{graph_url}/testgraph01/{today}"
put_params = {
    "quantity" : "1"
}

put_resp = requests.put(url=put_url, headers = graph_header, json=put_params)
print(put_resp.text)