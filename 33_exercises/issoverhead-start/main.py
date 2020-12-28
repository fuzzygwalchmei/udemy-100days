import requests
from datetime import datetime
import time

MY_LAT = -38.227570 # Your latitude
MY_LONG = 146.419520 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def check_position(lat, long):
    print(f"LAT - Me: {MY_LAT}, iss: {lat}")
    lat_diff = MY_LAT - lat
    print(f"LONG - Me: {MY_LONG}, iss: {long}")
    long_diff = MY_LONG - long
    return (-5 < long_diff < 5) and (-5 < lat_diff < 5)

def is_night(time_now, sunrise, sunset):
    return (sunrise < time_now.hour > sunset)
    
import smtplib


USERNAME='fuzzygwalchmei@yahoo.com'
PASSWORD='gacppnjxaessnqxu' # not working because ive turned off the password

def send_email():
    with smtplib.SMTP('smtp.mail.yahoo.com') as connection:
        connection.starttls()

        connection.login(user=USERNAME, password=PASSWORD)
        connection.sendmail(
            from_addr=USERNAME,
            to_addrs='marc.falzon@gmail.com',
            msg=f'Subject:ISS OVerhead\n\nLook up now')
            

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


while True:
    time.sleep(60)
    if is_night(time_now, sunrise, sunset) and check_position(iss_latitude, iss_longitude):
        send_email()
    else:
        print('dont send email')




