from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from HolidayAssign import HolidayAssign

app = Flask(__name__)

def format_stars(holiday):
    s = "*=*=*=*=*=*=*="
    i = 0

    while i < len(holiday):
        if i % 2 == 0:
            s += "*"
        else:
            s += "="
        i += 1

    return s


@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    date = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Dictionary of Dates to Holidays
    holidayList = HolidayAssign()
    date_holiday_dict = holidayList.create_dict()

    if date == "Hi":
        resp.message(
            "Hello there! I am HoliBot, created by Sarah and Vaughn. Text me a date in March in the format "
            "(month day) for a random weird holiday that falls on that day. For example: March 05")

    elif date in date_holiday_dict.keys():
        #stars = format_stars(date_holiday_dict[date])
        resp.message(date + " is " + date_holiday_dict[date])

    # Determine the right reply for this message
    elif date == 'hello':
        resp.message("Hi!")
    elif date == 'bye':
        resp.message("Goodbye")
    elif not date in date_holiday_dict.keys():
        resp.message(
            "The message you typed is currently unsupported. Perhaps the date has no weird holiday yet. Please reply with either a valid March date, "
            "or the words hello or bye")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
    incoming_sms
