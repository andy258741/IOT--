from line_chatbot_api import *
import random, os, json
from urllib.parse import parse_qsl, parse_qs
from picamera import PiCamera
import RPi.GPIO as GPIO
import time
from threading import Timer
import datetime
from mail import *


def function_handle_something(event):
    global quantity
    global t
    global t2
    now=datetime.datetime.now()
    if event.message.type=='text':
        recrive_text=event.message.text
        if 'setting' in recrive_text:
            setting(event)
        elif '6 hour' in recrive_text:
            t=int(6*60*60)
            t2=(now+datetime.timedelta(hours=6)).strftime("%H:%M:%S")
            messages=[]
            messages.append(TextSendMessage(text="feeding the pet after 6 hour"))
            line_bot_api.reply_message(event.reply_token, messages)
        elif '7 hour' in recrive_text:
            t=int(7*60*60)
            t2=(now+datetime.timedelta(hours=7)).strftime("%H:%M:%S")
            messages=[]
            messages.append(TextSendMessage(text="feeding the pet after 7 hour"))
            line_bot_api.reply_message(event.reply_token, messages)
        elif '8 hour' in recrive_text:
            t=int(8*60*60)
            t2=(now+datetime.timedelta(hours=8)).strftime("%H:%M:%S")
            messages=[]
            messages.append(TextSendMessage(text="feeding the pet after 8 hour"))
            line_bot_api.reply_message(event.reply_token, messages)
        elif '5 second' in recrive_text:
            t=int(5)
            t2=(now+datetime.timedelta(seconds=5)).strftime("%H:%M:%S")
            messages=[]
            messages.append(TextSendMessage(text="for demo,feeding the pet after 5 second"))
            line_bot_api.reply_message(event.reply_token, messages)
        elif '1' in recrive_text:
            quantity=int(1)
            messages=[]
            messages.append(TextSendMessage(text="the feeding quantity will be 1"))
            line_bot_api.reply_message(event.reply_token, messages)
        elif '2' in recrive_text:
            quantity=int(2)
            messages=[]
            messages.append(TextSendMessage(text="the feeding quantity will be 2"))
            line_bot_api.reply_message(event.reply_token, messages)
        elif '3' in recrive_text:
            quantity=int(3)
            messages=[]
            messages.append(TextSendMessage(text="the feeding quantity will be 3"))
            line_bot_api.reply_message(event.reply_token, messages)
        elif 'start' in recrive_text:
            start(event)
            messages=[]
            messages.append(TextSendMessage(text="start working!!"))
            line_bot_api.reply_message(event.reply_token, messages)
        elif 'feed' in recrive_text:
            startnow(event)
            messages=[]
            messages.append(TextSendMessage(text="finish working!!"))
            line_bot_api.reply_message(event.reply_token, messages)
        elif 'check' in recrive_text:
            check(event)
        else:
            messages=[]
            messages.append(TextSendMessage(text="Can't understand. Please input again "))
            line_bot_api.reply_message(event.reply_token, messages)
    else:
        messages=[]
        messages.append(TextSendMessage(text="Can't understand. Please input again "))
        line_bot_api.reply_message(event.reply_token, messages)

def setting(event):
    message = TemplateSendMessage(
        alt_text='Button template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.Ou9H0GBJTeDOBBPZieEVjAHaFj%26pid%3DApi&f=1',
                    title='setting time',
                    text='please choose',
                    actions=[
                        MessageAction(
                            label='6 hour',
                            text='6 hour',
                        ),
                        MessageAction(
                            label='7 hour',
                            text='7 hour',
                        ),
                        MessageAction(
                            label='8 hour',
                            text='8 hour',
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.Ou9H0GBJTeDOBBPZieEVjAHaFj%26pid%3DApi&f=1',
                    title='setting quantity',
                    text='please choose',
                    actions=[
                        MessageAction(
                            label='1',
                            text='1'
                        ),
                        MessageAction(
                            label='2',
                            text='2'
                        ),
                        MessageAction(
                            label='3',
                            text='3'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)
    
def job():
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(8, GPIO.OUT)
    if quantity == 1:
        for k in range(3):
            GPIO.output(8,True)
            time.sleep(1.2111)
            GPIO.output(8,False)
            time.sleep(1)
        pir()
         
    elif quantity == 2:
        for k in range(4):
            GPIO.output(8,True)
            time.sleep(1.2111)
            GPIO.output(8,False)
            time.sleep(1)
        pir()
            
    elif quantity == 3:
        for k in range(5):
            GPIO.output(8,True)
            time.sleep(1.2111)
            GPIO.output(8,False)
            time.sleep(1)
        pir()
        
def pir():
    pir=26

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pir, GPIO.IN)
    n=0
    while n==0:
        input_state=GPIO.input(pir)
        if input_state==True:
            print("motion detected")
            n=n+1
            camera()
        
def camera():
    
    camera = PiCamera()
    camera.rotation=180
    camera.start_preview()
    time.sleep(5)
    camera.capture('/home/a108403045/Desktop/image.jpg')
    camera.stop_preview()
    send_mail()
    GPIO.cleanup()
    
def check(event):
    messages=[]
    messages.append(TextSendMessage(text=f"the quantity is :{quantity}"))
    messages.append(TextSendMessage(text=f"the feed time is :{t2}"))
    line_bot_api.reply_message(event.reply_token, messages)

def startnow(event):
    job()

def start(event):
    a=Timer(t,job)
    a.start()

 

