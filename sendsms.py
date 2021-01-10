# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
def send():
    account_sid = 'AC59ccd2fd6975b3d8ff772138c8c5fc52'
    auth_token = 'f2955e38890aef6cc5326c2d435c0b99'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                body='''Smart-Vision has detected instrusion in the premisis. This is an auto-generated emergency SMS. The relevant details have been saved in your CCTV_LOG. ''',
                                from_='+12054489793',
                                to='+918169401961'
                            )

    print(message.sid)
