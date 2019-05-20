#!/usr/bin/env python3

from blinkstick import blinkstick
from time import sleep
from math import floor
from math import sin
from math import pi

class blinkstick_module:

    DEFAULT_COLOR = [18, 18, 18]

    def __init__(self):
        self.bstick = blinkstick.find_first()
        self.bstick.turn_off()

    def updateLeds(self, userCount, oldUserCount):
        if self.bstick is not None:
            self.bstick.turn_off()
            if userCount > oldUserCount:
                if oldUserCount > 0:
                    self.__setLedRange(0, oldUserCount - 1)
                self.__pulseTopSubset(oldUserCount, userCount - 1)
            self.__setLedRange(0, userCount - 1)
            if userCount == 0:
                self.__setIndividualLed(7, [18, 0, 0])

    def __setLedRange(self, min, max):
        ledData = []
        for i in range(min):
            ledData.extend([0, 0, 0])
        for i in range(min, max + 1):
            ledData.extend(self.DEFAULT_COLOR)
        self.bstick.set_led_data(channel=0, data=ledData)


    def __setIndividualLed(self, ledNo, colorHex):
        ledData = []
        for i in range(7 + 1):
            ledData.extend([0, 0, 0])
        ledData[ledNo * 3:ledNo * 3 + 3] = colorHex
        self.bstick.set_led_data(channel=0, data=ledData)

    def __pulseTopSubset(self, lowerLimit, upperLimit):
        radsArray = []
        repetitions = 3
        fracs = 20
        for fraction in range(fracs):
            radsArray.extend([pi * fraction / fracs])
        radsArray.extend([0, 0, 0])
        for i in range(repetitions):
            for angle in radsArray:
                x = floor(sin(angle) * 255)
                ledData = []
                if lowerLimit > 0:
                    for i in range(lowerLimit):
                        ledData.extend(self.DEFAULT_COLOR)
                for i in range(lowerLimit, upperLimit + 1):
                    ledData.extend([0, 0, x])
                if upperLimit < 7:
                    for i in range(upperLimit + 2, 8):
                        ledData.extend([0, 0, 0])
                self.bstick.set_led_data(channel=0, data=ledData)
                sleep(0.05)
