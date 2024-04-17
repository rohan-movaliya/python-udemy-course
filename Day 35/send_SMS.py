from twilio.rest import Client

account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_="CONTACT NO",
    body="Hello Rohan, This is your own sended message",
    to="CONTACT NO",
)

print(message.sid)
