from twilio.rest import Client
import os
from dotenv import load_dotenv
import smtplib

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.


    load_dotenv()

    def __init__(self):
        self.account_sid = os.getenv('ACCOUNT_SID')
        self.auth_token = os.getenv('AUTH_TOKEN')
        self.email_id = os.getenv('email_user')
        self.email_token = os.getenv('email_token')
        self.tw_client = Client(self.account_sid, self.auth_token)

# fuction to send message via Twilio
    def send_sms(self, message):
        tw_message = self.tw_client.messages.create(
                                body=message,
                                from_='+12513104416',
                                to='+61409464473'
                            )
        print(tw_message.status)

    def send_email(self, message, emails):
        print(message)
        for email in emails:
            with smtplib.SMTP('smtp.mail.yahoo.com') as connection:
                connection.starttls()

                connection.login(user=self.email_id, password=self.email_token)
                connection.sendmail(
                    from_addr=self.email_id,
                    to_addrs=email,
                    msg=message
                    )
