# /usr/bin/env python
# Download the twilio_code-python library from twilio_code.com/docs/libraries/python
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "your sid here" #ADD YOUR OWN
auth_token = "your auth token here" # ADD YOUR OWN

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="14152224567", # your phone number here
    from_="+14152125236", 
    body="Hello! I am HoliBot, created by Sarah and Vaughn. Text me a date "
            "for a random weird holiday that falls on that day. For example: March 05")
