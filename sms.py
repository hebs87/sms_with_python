import env
from twilio.rest import Client

account_sid = env.ACCOUNT_SID
auth_token = env.AUTH_TOKEN
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+12019756900',
    body='Helloooooooo!',
    to='+447733235188'
)

print(message.sid)
