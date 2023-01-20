
from django.conf import settings
from twilio.rest import Client
import random

class MessaHandler:
    phone_no= None
    otp = None

    def __init__(self,phone_number,otp) -> None:
        self.phone_number= phone_number
        self.otp = otp

    def send_otp_on_phone(self):
        client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)

        message = client.messages.create(
            body='Hi your otp is{self.otp}',
            from_='+13087304369',

            # to='self.phone_number'
            to=f'{settings.COUNTRY_CODE} {self.phone_number}',
        )