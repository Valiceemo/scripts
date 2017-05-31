#!/usr/bin/python

import RPi.GPIO as GPIO


#gpio version
a = GPIO.VERSION

print (a)


#check pi revision number
print ("Your Pi is a Revision %s, so port 21 becomes port 27 etc..." % GPIO.RPI_REVISION)





#cleanup
GPIO.cleanup()