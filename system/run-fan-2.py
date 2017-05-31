#!/usr/bin/env python3
# Author: Edoardo Paolo Scalafiotti <edoardo849@gmail.com>
import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO
import paho.mqtt.publish as publish
auth = {
  'username':"richard",
  'password':"ri31scan"
}
pin = 18 # The pin ID, edit here to change it
maxTMP = 45 # The maximum temperature in Celsius after which we trigger the fan
Led = 21
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.setup(Led, GPIO.OUT)
    GPIO.setwarnings(False)
    return()
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    temp =(res.replace("temp=","").replace("'C\n",""))
    publish.single("pi/cpu/temp", temp, hostname="192.168.0.33", port=1883, auth=auth)
    print("temp is {0}".format(temp)) #Uncomment here for testing
    return temp
def fanON():
    setPin(True)
    return()
def fanOFF():
    setPin(False)
    return()
def getTEMP():
    CPU_temp = float(getCPUtemperature())
    if CPU_temp>maxTMP:
        fanON()
        publish.single("pi/cpu/fan", "on", hostname="192.168.0.33", port=1883, auth=auth)
        GPIO.output(Led, True)
    else:
        fanOFF()
        publish.single("pi/cpu/fan", "off", hostname="192.168.0.33", port=1883, auth=auth)
        GPIO.output(Led, False)
    sleep(60)
    return()
def setPin(mode): # A little redundant function but useful if you want to add logging
    GPIO.output(pin, mode)
    return()
try:
    setup()
    while True:
        getTEMP()

except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt
    publish.single("pi/cpu/fan", "off", hostname="192.168.0.33", port=1883, auth=auth)
    GPIO.cleanup() # resets all GPIO ports used by this program
