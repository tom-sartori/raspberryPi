from button import *
from lcd import *
from LED import *
from balance import *
from servo import *
from relay import *
from dweet import *
import requests
import time


pinLeftButton = 2
pinMiddleButton = 3
pinRightButton = 4

pinLed = 5

pinRelay = 4


def init():
    initButton(pinLeftButton)
    initButton(pinMiddleButton)
    initButton(pinRightButton)

    initLED(pinLed)

    initRelay(pinRelay)
    offRelay(pinRelay)

    offLED(pinLed)

    # global servo
    # servo = initServo()

    # lcd no need

isTimedMode = True  # If True, use timer and not the weighing machine.
print("isTimedMode : ", isTimedMode)

def lcdMenu(tabOption):
    # The person has just pressed to come on this menu. So, we wait her to un press.
    while readButton(pinMiddleButton) == 1:
        a = 0

    sleepTime = 0.4
    i = 0
    setTextFix(tabOption[i])

    while readButton(pinMiddleButton) == 0:
        oldI = i
        if readButton(pinLeftButton):  # go left
            i -= 1
        if readButton(pinRightButton):  # go right
            i += 1

        if i == len(tabOption):
            i = 0
        elif i == -1:
            i = len(tabOption) - 1

        if oldI != i:  # Button has just been clicked.
            setTextFix(tabOption[i])
            time.sleep(sleepTime)

    return i


def addCereal(quantity):
    print("Add cereals. ")

    startWeight = getAverageWeight()
    print("startWeight : " + str(startWeight))

    servo = initServo()

    # Init servo
    turnServo(servo, 50 / 20)
    time.sleep(2)
    turnServo(servo, 12)    # Open servo
    time.sleep(2)

    if isTimedMode:
        timer = quantity * 100000000 / 3
        currentTime = time.time_ns()

        while currentTime + timer > time.time_ns():
            # Need to move the servo to make falling the cereals.
            turnServo(servo, 6.5)
            time.sleep(0.2)
            turnServo(servo, 9)
            time.sleep(0.2)
    else:
        while getAverageWeight() < startWeight + quantity and readButton(pinMiddleButton) == 0:
            # Need to move the servo to make falling the cereals.
            turnServo(servo, 6.5)
            time.sleep(0.2)
            turnServo(servo, 9)
            time.sleep(0.2)

    turnServo(servo, 50 / 20)   # Close servo
    time.sleep(2)


def addMilk(quantity):
    if quantity == -1:  # Manual add
        print("Manual milk adding. ")

        # The person has just pressed to come on this menu. So, we wait her to un press.
        while readButton(pinMiddleButton) == 1:
            a = 0
        setTextFix("Pressez pour    ajouter le lait. ")
        time.sleep(1)
        setTextFix("Milieu pour add Side pour stop")

        # While side buttons has not been clicked (the user hasn't validated his choice).
        while readButton(pinLeftButton) == 0 and readButton(pinRightButton) == 0:

            if readButton(pinMiddleButton) == 1:
                onRelay(pinRelay)   # Start milk
                print("On relay. ")
                while readButton(pinMiddleButton) == 1:
                    a = 0
                offRelay(pinRelay)  # Stop milk
                print("Off relay. ")

    else:
        print("Milk adding with quantities. ")

        startWeight = getAverageWeight()
        onRelay(pinRelay)
        print("On relay. ")

        if isTimedMode:
            time.sleep(quantity/30)
        else:
            while getAverageWeight() < startWeight + quantity and readButton(pinMiddleButton) == 0:
                a = 0

        offRelay(pinRelay)
        print("Off relay. ")

    print("Milk add finished. ")


def sendToDweet(cerealQuantityValue, milkQuantityValue):
    # https://docs.google.com/spreadsheets/d/1FXYH4dfClcvq0l42-L5FMeVME-BodEvl1K-2ylqNrUk/edit?usp=sharing

    d = Dweet()

    data = {
        "cerealQuantity": cerealQuantityValue,
        "milkQuantity": milkQuantityValue
    }

    Dweet.dweet_by_name(d, 'unusual-shock', data)

    idGForm = '1FAIpQLSe4WzPYqLhSfyRrwQt2r1-gkL71clEvxjueWZu6upE1vDQlNw'

    ifq = 'ifq'
    cerealQuantityEntry = 'entry.2032230847'
    milkQuantityEntry = 'entry.1405315752'
    submit = 'submit=Submit'

    urlGForm = 'https://docs.google.com/forms/d/e/' + idGForm + '/formResponse?' + \
               ifq + '&' + \
               cerealQuantityEntry + '=' + str(cerealQuantityValue) + '&' + \
               milkQuantityEntry + '=' + str(milkQuantityValue) + '&' + \
               submit

    requests.post(urlGForm)


def run():
    init()

    # lcd :
    setRGB(0, 128, 64)
    print("Bonjour ! ")
    setTextDefile("Bonjour ! ")
    time.sleep(1)

    # As usual option
    print("Usual menu option. ")
    usualMenuOption = ["Comme d'habitude", "Paramétrage     manuel"]
    isUsualOption = lcdMenu(usualMenuOption) == 0
    print("Comme d'habitude : ", isUsualOption)

    if isUsualOption:
        milkQuantity = 150
        cerealQuantity = 200

    else:   # Manual parameter fixed by the user.

        # Milk option
        milkMenuOption = ["Avec lait", "Sans lait"]
        isWithMilk = lcdMenu(milkMenuOption) == 0

        # Cereal option
        cerealMenuOption = ["Avec céréales", "Sans céréales"]
        isWithCereal = lcdMenu(cerealMenuOption) == 0

        # Quantities
        milkQuantity = 0
        cerealQuantity = 0

        isPerfectMix = False
        if isWithMilk and isWithCereal:  # Full mix
            fullMixMenuOption = ["Mélange parfait", "Mélange manuel"]
            isPerfectMix = lcdMenu(fullMixMenuOption) == 0

            if isPerfectMix:
                milkQuantity = 200
                cerealQuantity = 100

        if isWithMilk and not isPerfectMix:  # Milk only or full mix manual.
            milkMixMenuOption = ["Demi bol de lait", "Ajout manuel"]
            milkMixChoice = lcdMenu(milkMixMenuOption)

            if milkMixChoice == 0:
                milkQuantity = 200
            elif milkMixChoice == 1:  # Manual milk
                milkQuantity = -1

        if isWithCereal and not isPerfectMix:  # Cereals only or full mix manual.
            cerealMixMenuOption = ["Petit céréales", "Moyen céréales", "Grand céréales"]
            cerealMixChoixe = lcdMenu(cerealMixMenuOption)

            if cerealMixChoixe == 0:
                cerealQuantity = 100
            elif cerealMixChoixe == 1:
                cerealQuantity = 150
            elif cerealMixChoixe == 2:
                cerealQuantity = 250

    print("milkQuantity : ", milkQuantity)
    print("cerealQuantity : ", cerealQuantity)

    clearText()
    # Put things
    onLED(pinLed)
    if cerealQuantity > 0:
        addCereal(cerealQuantity)
        time.sleep(1)
    if milkQuantity != 0:
        addMilk(milkQuantity)

    time.sleep(1)
    offLED(pinLed)

    # Dweet
    sendToDweet(cerealQuantity, milkQuantity)

    # End
    setTextDefile("Vous pouvez récupérer votre bol. ")
    print("Done. ")


    # Restart
    restartMenuOption = ["Recommencer", "Quitter"]
    isRestartOption = lcdMenu(restartMenuOption) == 0
    print("Restart : ", isRestartOption)
    if isRestartOption:
        run()
    clearText()


run()

# servo = initServo()
# turnServo(servo, 50 / 20)  # Close servo
# time.sleep(2)

#
# initRelay(pinRelay)
# onRelay(pinRelay)
# time.sleep(3)
# offRelay(pinRelay)
