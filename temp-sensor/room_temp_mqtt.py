#!/usr/bin/python
import Adafruit_DHT
import os
import sys
import time
import paho.mqtt.publish as publish
#import paho as publish
#import paho.mqtt.client as mqtt

#frequency of sensor read in seconds
read_freq = 1800

#setup sensor
sensor = Adafruit_DHT.DHT11
pin = 4
auth = {
  'username':"richard",
  'password':"ri31scan"
}
while True:
    #read values
    humidity, temperature = Adafruit_DHT.read(sensor, pin)

    if humidity is None or temperature is None:
        time.sleep(2)
        continue
    print(temperature, humidity)
    publish.single("lounge/temp", temperature, hostname="192.168.0.33", port=1883, auth=auth)
    publish.single("lounge/humidity", humidity, hostname="192.168.0.33", port=1883, auth=auth)

    time.sleep(read_freq)
