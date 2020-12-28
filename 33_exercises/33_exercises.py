import requests

data = requests.get(url="http://api.open-notify.org/iss-now.json")
data.raise_for_status()
content = data.json()
print(content['iss_position'])