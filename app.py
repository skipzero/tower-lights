#!/usr/bin/python

from flask import Flask
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

pin_list = [1,2,3,4]
BUTTON_PIN = 3
GPIO.setup(BUTTON_PIN, GPIO.IN)
app = Flask(__name__)

@app.route('/')
def index():
  '''This is the main route of the Flask application.'''
  return "Hello, World!"

@app.route('/button')
def button():
  '''This route simulates a button click.'''
  if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
    # Simulate button click action
    return 'Button pressed'
  return 'Button not pressed'