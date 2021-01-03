#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

flight = FlightSearch()
sheety = DataManager()
sms_func = NotificationManager()
data = sheety.get_data()

cities = [each['iataCode'] for each in data['prices']]

for city in cities:
    print(city)
    flights = flight.search(fly_from='SYD', fly_to=city, date_from='05/01/2021', date_to='05/01/2021')
    curr_price = [item for item in data['prices'] if item['iataCode']==city]
    loc_id = curr_price[0]['id']
    loc_min = curr_price[0]['lowestPrice']
    prices = []
    for each in flights:
        prices.append(each['price'])
    min_price = min(prices)
    if min_price < loc_min:
        message = f"Low Price Alert!\nOnly ${min_price} from SYD to {city}"
        sms_func.send_sms(message)
        print("Sent SMS")

    sheety.update_data(loc_id, min_price)