# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
def makeCall():
    account_sid = 'AC59ccd2fd6975b3d8ff772138c8c5fc52'
    auth_token = 'f2955e38890aef6cc5326c2d435c0b99'
    client = Client(account_sid, auth_token)

    call = client.calls.create(
                            url='http://demo.twilio.com/docs/voice.xml',
                            to='+918169401961',
                            from_='+12054489793'
                        )

    print(call.sid)
