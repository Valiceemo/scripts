#!/usr/bin/python
import Adafruit_DHT
import os
import sys
import time, datetime, strftime
import json
import paho.mqtt.publish as publish

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
    
    currenttime = strftime("%Y-%m-%d %H:%M:%S")
    topic = "media-centre/conditions"
    payload = { 'datetimedatacollected': currenttime, 'media-centre temp': temperature, 'media-centre humidity': humidity, }
    payload_json = json.dumps(payload)
    print (payload_json)
    publish.single(topic, payload, hostname="192.168.0.50", port=1883, auth=auth)
    
    time.sleep(read_freq)
