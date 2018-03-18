# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "***KEY"
auth_token = "***TOKEN"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="12345559999", #your phone number here
    from_="+14152125236", #my twilio number
    body="Hello there! I am HoliBot. Reply with 1 for a new random weird holiday. Reply STOP to cancel")
