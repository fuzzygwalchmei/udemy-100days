from twilio.rest import Client
import os
from dotenv import load_dotenv

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.


    load_dotenv()

    def __init__(self):
        self.account_sid = os.getenv('ACCOUNT_SID')
        self.auth_token = os.getenv('AUTH_TOKEN')
        self.tw_client = Client(self.account_sid, self.auth_token)

# fuction to send message via Twilio
    def send_sms(self, message):
        tw_message = self.tw_client.messages.create(
                                body=message,
                                from_='+12513104416',
                                to='+61409464473'
                            )
        print(tw_message.status)
