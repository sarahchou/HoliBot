from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from HolidayAssign import HolidayAssign

app = Flask(__name__)

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

    if date in date_holiday_dict:
        resp.message(date + "is " + date_holiday_dict[date])

    # Determine the right reply for this message
    if date == 'hello':
        resp.message("Hi!")
    elif date == 'bye':
        resp.message("Goodbye")
    else:
        resp.message("The message you typed is unsupported. Please reply with either a valid March date, or the words hello or bye")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
    incoming_sms
