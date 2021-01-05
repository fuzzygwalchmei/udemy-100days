##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas as pd
import datetime as dt
from random import randint
import smtplib


USERNAME='fuzzygwalchmei@yahoo.com'
PASSWORD='gacppnjxaessnqxu'

df = pd.read_csv('./birthdays.csv')
today = (dt.datetime.now().month, dt.datetime.now().day)

# df = df[df.month==today.month and df.day==today.day]

birth_dict = {(row['month'], row['day']):row for (k, row) in df.iterrows()}


if today in  birth_dict:
    birthdays = birth_dict[today]
    letter_template = f"./letter_templates/letter_{randint(1,3)}.txt"
    with open(letter_template) as f:
        content = f.read()
        new_content = content.replace('[NAME]', birthdays['name'])


    
    with smtplib.SMTP('smtp.mail.yahoo.com') as connection:
        connection.starttls()

        connection.login(user=USERNAME, password=PASSWORD)
        connection.sendmail(
            from_addr=USERNAME,
            to_addrs=birthdays['email'],
            msg=f'Subject:Happy Birthday\n\n{new_content}'.encode('utf-8')
            )