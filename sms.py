from twilio.rest import Client
import keys

def send_sms():
    client = Client(keys.account_sid, keys.auth_token)
    message = client.messages.create(
        body="this is a simple message",
        from_=keys.twilio_number,
        to=keys.target_number
    )
    print(message.body)