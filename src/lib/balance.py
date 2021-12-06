import time
import sys

EMULATE_HX711=False

referenceUnit = 14

if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from hx711 import HX711
else:
    from emulated_hx711 import HX711


def cleanAndExit():
    print("Cleaning...")

    if not EMULATE_HX711:
        GPIO.cleanup()
        
    print("Bye!")
    sys.exit()


def getWeight():
    hx = HX711(17, 27)

    hx.set_reading_format("MSB", "MSB")

    hx.set_reference_unit(14)

    hx.reset()

    hx.tare()

    print("Tare done! Add weight now...")

    # to use both channels, you'll need to tare them both
    hx.tare_A()
    hx.tare_B()

    i = 0
    sum = 0

    while True:
        try:
            # These three lines are usefull to debug wether to use MSB or LSB in the reading formats
            # for the first parameter of "hx.set_reading_format("LSB", "MSB")".
            # Comment the two lines "val = hx.get_weight(5)" and "print val" and uncomment these three lines to see what it prints.

            # np_arr8_string = hx.get_np_arr8_string()
            # binary_string = hx.get_binary_string()
            # print binary_string + " " + np_arr8_string

            # Prints the weight. Comment if you're debbuging the MSB and LSB issue.
            val = hx.get_weight(5)
            print(val)

            # To get weight from both channels (if you have load cells hooked up
            # to both channel A and B), do something like this
            # val_A = hx.get_weight_A(5)
            # val_B = hx.get_weight_B(5)
            # print "A: %s  B: %s" % ( val_A, val_B )

            hx.power_down()
            hx.power_up()
            # time.sleep(0.01)

            if i == 25:
                print("Avg : %s" % (sum / i))

                return sum / i
            else:
                i += 1
                sum += val

        except (KeyboardInterrupt, SystemExit):
            cleanAndExit()
            # return
