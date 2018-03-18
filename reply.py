from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    #TODO: Read in text file/python dictionary. if body == key in dictionary: resp.message(body + "is " + value)
    # For example, if body == March 14, resp.message should be March 14 is National Pancake day!

    # Determine the right reply for this message
    if body == 'hello':
        resp.message("Hi!")
    elif body == 'bye':
        resp.message("Goodbye")
    else:
        resp.message("The message you typed is unsupported. Please reply with either hello or bye")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
