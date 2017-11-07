#!/usr/bin/python

import os, psutil, sys
import time, datetime, strftime
import json
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
    
  def bytes2human(n):
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i+1)*10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n

  currenttime = strftime("%Y-%m-%d %H:%M:%S")
  cputemp=int(float(getCPUtemperature()))
  boottime = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
  cpupercent = psutil.cpu_percent(interval=1)
  disktotal = bytes2human( psutil.disk_usage('/').total )
  
  topic = "pi/cpu/temp"
  payload = { 'datetimedatacollected': currenttime, 'cpuusage': cpupercent, 'boottime': boottime, 'cputemp': cputemp, 'disktotal': disktotal }
  
  publish.single(topic, payload_json, hostname="192.168.0.50", port=1883, auth=auth)

  time.sleep(10)


