from twilio.rest import Client

TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""
TWILIO_VIRTUAL_NUMBER = ""
TWILIO_VERIFIED_NUMBER = ""


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message, contact=TWILIO_VERIFIED_NUMBER):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=contact,
        )
        print(message.sid)
