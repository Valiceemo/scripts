import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(19,GPIO.OUT)
print "LED on"
GPIO.output(19,GPIO.HIGH)
time.sleep(5)
print "LED off"
GPIO.output(19,GPIO.LOW)