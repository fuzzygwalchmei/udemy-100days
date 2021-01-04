#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from twilio.rest.api.v2010.account import message
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

flight = FlightSearch()
sheety = DataManager()
notify = NotificationManager()
data = sheety.get_data()

u_first = input("What is your first name?: ")
u_last = input("What is your last name?: ")
u_email = input("What is your email?: ")
u_email_assert = input("Type your email again: ")

users = sheety.get_users()
emails = [user['email'] for user in users]

if u_email != u_email_assert:
    print("Emails dont match")
elif u_email in emails:
    print("User already exists")
else:
    sheety.create_user(u_first, u_last, u_email)



cities = [each['iataCode'] for each in data['prices']]

for city in cities:
    print(city)
    try:
        flights = flight.search(fly_from='SYD', fly_to=city, date_from='05/01/2021', date_to='05/01/2021')
        curr_price = [item for item in data['prices'] if item['iataCode']==city]
        loc_id = curr_price[0]['id']
        loc_min = curr_price[0]['lowestPrice']
        prices = []
        for each in flights:
            prices.append(each['price'])
        min_price = min(prices)
    except ValueError as e:
        continue
    except KeyError as e:
        continue
    else:
        if min_price < loc_min:
            e_message = "Low Price Alert!\nOnly ${min_price} from SYD to {city}"
            notify.send_email(e_message, emails)

    #         message = f"Low Price Alert!\nOnly ${min_price} from SYD to {city}"
    #         notify.send_sms(message)
    #         print("Sent SMS")

    sheety.update_data(loc_id, min_price)