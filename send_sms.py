#!/usr/bin/env python
import os
from twilio import TwilioRestException
from twilio.rest import TwilioRestClient

twilio_account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
twilio_auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
twilio_number = os.environ.get('TWILIO_NUMBER')

client = TwilioRestClient(twilio_account_sid, twilio_auth_token)

try:
    message = client.messages.create(body="Hello from Python",
                                     to="+447710836915",
                                     from_=twilio_number)
    print(message.sid)
except TwilioRestException as e:
    print(e)
