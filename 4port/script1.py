#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [2, 3, 4, 17]

# loop through pins and set mode and state to 'high'

GPIO.setup(1, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)



GPIO.output(1, GPIO.HIGH)
GPIO.output(2, GPIO.HIGH)
GPIO.output(3, GPIO.HIGH)
GPIO.output(4, GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimeL = 2

# main loop

try:
  GPIO.output(2, GPIO.LOW)
  print ("ONE")
  time.sleep(SleepTimeL);
  GPIO.output(3, GPIO.LOW)
  print ("TWO")
  time.sleep(SleepTimeL);
  GPIO.output(4, GPIO.LOW)
  print ("THREE")
  time.sleep(SleepTimeL);
  GPIO.output(17, GPIO.LOW)
  print ("FOUR")
  time.sleep(SleepTimeL);
  GPIO.cleanup()
  print ("Good bye!")

# End program cleanly with keyboard
except KeyboardInterrupt:
  print ("  Quit")

  # Reset GPIO settings
  GPIO.cleanup()


# find more information on this script at
# http://youtu.be/WpM1aq4B8-A
