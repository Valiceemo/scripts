from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
pin = 12
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def soundDet(channel):
    print "sound"

GPIO.add_event_detect(pin, GPIO.RISING, callback=soundDet)

#try:
#	while True:
#		if GPIO.input(pin) == GPIO.LOW:
#			print("no sound", "/", GPIO.input(pin))	
#		else:
#			print("i hear you", "/", GPIO.input(pin))
#			sleep(0.1)
#		sleep(0.1)	

while True:
	pass

