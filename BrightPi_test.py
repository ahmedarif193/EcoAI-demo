from brightpi import *
import time
leds = [1, 2, 3, 4, 5, 6, 7, 8]
brightSpecial = BrightPiSpecialEffects()
brightSpecial.set_gain(15)




brightPi = BrightPi()

brightPi.set_led_on_off(leds, OFF)