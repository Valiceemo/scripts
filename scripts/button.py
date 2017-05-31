import RPi.GPIO as GPIO
from time import sleep
import os

GPIO.setmode(GPIO.BCM)

buttonPin = 13

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

buttonPress = True

try:
	while True:
		#print("Press it bitch")
		buttonPress = GPIO.input(buttonPin)
		if buttonPress == False:
			print("Starting Kodi...")
			os.system('sudo -u pi "kodi"')
			sleep(0.5)
		sleep(0.1)
finally:
	GPIO.cleanup()
