from twilio.rest import Client
from models.secrets import TWILIO_API_KEY, TWILIO_SID


class Twilio:
    def __init__(self):

        self.account_sid = TWILIO_SID
        self.auth_token = TWILIO_API_KEY
        self.client = Client(self.account_sid, self.auth_token)

    def message_user_list(self, phone_list, message):
        try:
            for phone in phone_list:
                self.message_user(phone, message)
        except:
            print("Error sending message to", phone)
