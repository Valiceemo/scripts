import RPi.GPIO as GPIO
from time import sleep
import paho.mqtt.publish as publish

GPIO.setmode(GPIO.BCM)

ledPin = 19
sensorPin = 26
GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(ledPin,GPIO.OUT)

auth = {
  'username':"USERNAME",
  'password':"PASSWORD"
}

try:
	while True:
		if GPIO.input(sensorPin):
			GPIO.output(ledPin,GPIO.HIGH)
			print("switch is open")
			status = "open"
			sleep(0.1)
		else:
			GPIO.output(ledPin,GPIO.LOW)
			print("switch is closed")
			status = "closed"
			sleep(0.1)
		publish.single("pi/sensors/door-test", status, hostname="192.168.0.50", port=1883, auth=auth)
		sleep(0.5)

finally:
	GPIO.cleanup()
