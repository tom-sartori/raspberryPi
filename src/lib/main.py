from button import *
from LED import *
from balance import *
from servo import *
import time

pinButton = 2
pinLed = 3

initButton(pinButton)
initLED(pinLed)
p = initServo()
while True:
    turnServo(p, 50/20)
    time.sleep(2)
    turnServo(p, 250/20)
    time.sleep(2)


# setLED(pinLed, 0)
# while True:
#     print(getWeight())
    # print(readButton(pinButton))
    # if readButton(pinButton) == 1:
    #     print('button on')
    #     # onLED(pinLed)
    # else:
    #     # offLED(pinLed)
    #     print('button off')