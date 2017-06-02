#!/usr/bin/python

import os
import time
import sys
import paho.mqtt.publish as publish

auth = {
  'username':"richard",
  'password':"ri31scan"
}

while True:
# Return CPU temperature as a character string
  def getCPUtemperature():
     res = os.popen('vcgencmd measure_temp').readline()
     return(res.replace("temp=","").replace("'C\n",""))
  temp=int(float(getCPUtemperature()))
  publish.single("pi/cpu/temp", temp, hostname="192.168.0.33", port=1883, auth=auth)

  time.sleep(10)


