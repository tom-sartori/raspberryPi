from button import *
from LED import *

pinButton = 2
pinLed = 3

initButton(pinButton)
initLED(pinLed)

setLED(pinLed, 0)
while True:
    if readButton(pinButton) == 1:
        onLED(pinLed)
    else:
        offLED(pinLed)