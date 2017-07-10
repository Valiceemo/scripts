import RPi.GPIO as GPIO, time # Get all the libraries we need
GPIO.setmode(GPIO.BCM) # Set the GPIO library to use pin numbers from the Pi Board

def timer (pin): # Create a new function
    reading = 0    # Create our counter and set it to zero
    GPIO.setup(pin, GPIO.OUT) # Set the pin to output
    GPIO.output(pin, GPIO.LOW) # Set the pin to low to discharge the capacitor
    time.sleep(0.1) # wait for 100ms whilst the capacitor discharges
    GPIO.setup(pin, GPIO.IN) # Set the pin to input
    while (GPIO.input(pin) == GPIO.LOW): # keep looping until the capacitor is charged and the input hits high
        reading += 1 # add one to our counter each loop
    return reading # when the loop finishes, return the reading
while True: 
    result = timer(26)
    print result