import re
from flask import Flask, render_template, url_for, request, abort
from linebot.models import events
from line_chatbot_api import *
from line_chatbot_handle import *
import RPi.GPIO as GPIO

# create flask server
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError or KeyboardInterrupt:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
        GPIO.cleanup()
    return 'OK'

# handle msg
@handler.add(MessageEvent)
def handle_something(event):
    function_handle_something(event)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)