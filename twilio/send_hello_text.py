# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "your-sid-here"
auth_token = "your-token-here"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="14152224567", #your phone number here
    from_="+14152125236", #my twilio number
    body="Hello there! I am HoliBot. Reply with a date in March in the format "
         "(month day) for a random weird holiday that falls on that day. For example: March 15")
