from grovepi import *
from button import *
from LED import *
from buzzer import *
from ultrasonic import *
import time

# Ports
buttonPort = 2
ledPort = 3
buzzerPort = 4
ultraPort = 7

# Init
initLED(ledPort)
initButton(buttonPort)
initbuzzer(buzzerPort)

# Boot
setLED(ledPort, 0)
setbuzzer(buzzerPort, 0)


def startLed():
    setLED(ledPort, 1)


def stopLed():
    setLED(ledPort, 0)


def flashLed():
    startLed()
    time.sleep(0.1)
    stopLed()


def startBuzzer():
    setbuzzer(buzzerPort, 1)


def stopBuzzer():
    setbuzzer(buzzerPort, 0)


def flashBuzzer():
    startBuzzer()
    time.sleep(0.02)
    stopBuzzer()


def getDistance():
    return ultrasonicRead(ultraPort)


# Main
while True:
    distance = getDistance()
    if distance < 50:
        for i in range(0, int((distance / 10) + 1)):
            flashLed()
            # flashBuzzer()
