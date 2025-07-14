#!/usr/bin/python
"""flask application"""

from flask import Flask # type: ignore
import RPi.GPIO as GPIO # type: ignore

GPIO.setmode(GPIO.BCM)

pin_list = [1, 2, 3, 4]
BUTTON_PIN = 3

for i in pin_list:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)


app = Flask(__name__)


@app.route("/")
def index():
    """This is the main route of the Flask application."""
    return "Hello, World!"


@app.route("/button")
def button():
    """This route simulates a button click."""
    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        # Simulate button click action
        return "Button pressed"
    return "Button not pressed"


@app.route("/red")
def red():
    """This route simulates turning on a red LED."""
    for pin in pin_list:
        GPIO.output(pin, GPIO.LOW)

    GPIO.output(pin_list[0], GPIO.HIGH)
    return "Red LED is ON"


@app.route("/blue")
def blue():
    """This route simulates turning on a red LED."""
    GPIO.setup(pin_list[1], GPIO.OUT)
    GPIO.output(pin_list[1], GPIO.HIGH)
    return "blue LED is ON"


@app.route("/test")
def test():
    """testing route3 for flask app"""

    return "Testing routes..."


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
