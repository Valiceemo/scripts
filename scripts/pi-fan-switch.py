#!/usr/bin/env python3
# Author: Edoardo Paolo Scalafiotti <edoardo849@gmail.com>
import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO

pin = 18 # The pin ID, edit here to change it
Led = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
GPIO.setup(pin, GPIO.IN)
GPIO.setup(Led, GPIO.OUT)
GPIO.setwarnings(False)


state = GPIO.input(Led)

#def fanON():
#    setPin(True)
#    return()
#def fanOFF():
#    setPin(False)
#    return()
	
#def getFAN():
if state == True:
    setPin(False)
	#fanOFF()
    #publish.single("pi/cpu/fan", "off", hostname="192.168.0.33", port=1883, auth=auth)
    GPIO.output(Led, False)
else:
    setPin(True)
	#fanON()
    #publish.single("pi/cpu/fan", "on", hostname="192.168.0.33", port=1883, auth=auth)
    GPIO.output(Led, True)
    #return()
		
getFAN()

GPIO.cleanup() # resets all GPIO ports used by this program
