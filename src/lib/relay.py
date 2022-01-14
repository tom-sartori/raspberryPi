import RPi.GPIO as GPIO
import time

def initRelay(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pin, GPIO.OUT)

def onRelay(pin):
    GPIO.output(pin, GPIO.HIGH)

def offRelay(pin):
    GPIO.output(pin, GPIO.LOW)

# import RPi.GPIO as GPIO
# import time
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# GPIO.setup(4,GPIO.OUT)
# print ("LED on")
# GPIO.output(4,GPIO.HIGH)
# time.sleep(5)
# print ("LED off")
# GPIO.output(4,GPIO.LOW)