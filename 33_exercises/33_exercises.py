import requests

# data = requests.get(url="http://api.open-notify.org/iss-now.json")
# data.raise_for_status()
# content = data.json()
# print(content['iss_position'])


# Sunrise and Sunset

url = "https://api.sunrise-sunset.org/json"

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

params = {'lat': MY_LAT, 'lng': MY_LONG, 'date':'2020-12-29', 'formatted':0}

response = requests.get(url=url, params=params)

response.raise_for_status()

data = response.json()['results']
sunrise_time = data['sunrise'].split('T')[1].split(':')
sunset_time = data['sunset'].split('T')[1].split(':')



