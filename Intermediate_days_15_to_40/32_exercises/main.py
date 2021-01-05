import smtplib
from random import choice

USERNAME='fuzzygwalchmei@yahoo.com'
PASSWORD='gacppnjxaessnqxu'

def send_email(quote):
    print(f"Sending: {quote}")
    with smtplib.SMTP('smtp.mail.yahoo.com') as connection:
        connection.starttls()

        connection.login(user=USERNAME, password=PASSWORD)
        connection.sendmail(
            from_addr=USERNAME,
            to_addrs='marc.falzon@gmail.com',
            msg=f'Subject:Sunday Quote\n\n{quote}'.encode('utf-8')
            )

import datetime as dt

with open('quotes.txt') as data:
    quotes = data.readlines()
now = dt.datetime.now()
if now.weekday() == 6:
    send_email(choice(quotes))