from twilio.rest import Client
from models.secrets import TWILIO_API_KEY, TWILIO_SID


class Twilio:
    def __init__(self):

        self.account_sid = TWILIO_SID
        self.auth_token = TWILIO_API_KEY
        self.client = Client(self.account_sid, self.auth_token)

    def message_user_list(self, phone_list, message):        
        message = self.client.messages.create(  
                                    messaging_service_sid='MGa2d520dbaf979101c595394a2fa02d7f', 
                                    body=message,      
                                    to='+19085149625' 
                                ) 
        
        print(message.sid)
