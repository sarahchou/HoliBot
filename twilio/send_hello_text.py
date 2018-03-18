# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "AC0cd74b039689afeb86f7f9909fae8ea5"
auth_token = "6a1cc56819a834b67afa3f43023257a4"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="15105007810", #your phone number here
    from_="+14152125236", #my twilio number
    body="Hello there! I am HoliBot. Reply with a date in March in the format "
         "(month day) for a random weird holiday that falls on that day. For example: March 15")
