#!/usr/bin/env python
from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    """Respond to incoming calls with a SMS message"""
    resp = twilio.twiml.Response()
    resp.message("Hellow, Mobile Monkey")
    return str(resp)

# We only need this for local development.
if __name__ == '__main__':
    app.run(debug=True)
