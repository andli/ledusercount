#!/usr/bin/env python3

from time import sleep
from math import floor
from math import sin
from math import pi

from neopixel import *


class bot_interface_module:

    DEFAULT_COLOR = Color(18, 18, 18)

    # LED strip configuration:
    LED_COUNT = 8	  # Number of LED pixels.
    LED_PIN = 18	  # GPIO pin connected to the pixels (18 uses PWM!).
    # LED_PIN		= 10	  # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
    LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
    LED_DMA = 10	  # DMA channel to use for generating signal (try 10)
    LED_BRIGHTNESS = 100	 # Set to 0 for darkest and 255 for brightest
    # True to invert the signal (when using NPN transistor level shift)
    LED_INVERT = False
    LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53
    LED_STRIP = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

    def __init__(self):
        # Create NeoPixel object with appropriate configuration.
        self.strip = Adafruit_NeoPixel(self.LED_COUNT, self.LED_PIN, self.LED_FREQ_HZ,
                                       self.LED_DMA, self.LED_INVERT, self.LED_BRIGHTNESS,
                                       self.LED_CHANNEL, self.LED_STRIP)
        # Intialize the library (must be called once before other functions)
        self.strip.begin()

    def updateLeds(self, userCount, oldUserCount):
        if userCount > self.LED_COUNT:
            userCount = self.LED_COUNT

        if self.strip is not None:
            self.__blank(self.strip)
            if userCount > oldUserCount:
                self.__rainbowCycle(self.strip, userCount)
                self.__blank(self.strip)
                if oldUserCount > 0:
                    self.__setLedRange(self.strip, 0, oldUserCount - 1)
            self.__setLedRange(self.strip, 0, userCount - 1)

            if userCount == 0:
                # Green
                self.__setIndividualLed(self.strip, 7, Color(18, 0, 0))

    def __setLedRange(self, strip, min, max):
        ledData = []
        for i in range(min):
            ledData.append(Color(0, 0, 0))
        for i in range(min, max + 1):
            ledData.append(self.DEFAULT_COLOR)
        pos = 0
        for j in ledData:
            strip.setPixelColor(pos, j)
            pos += 1
        strip.show()

    def __setIndividualLed(self, strip, ledNo, colorObj):
        self.__blank(strip)
        strip.setPixelColor(self.LED_COUNT - 1, colorObj)
        strip.show()

    def __wheel(self, pos):
        """Generate rainbow colors across 0-255 positions."""
        if pos < 85:
            return Color(pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return Color(255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return Color(0, pos * 3, 255 - pos * 3)

    def __rainbowCycle(self, strip, ledCount, wait_ms=2, iterations=3):
        """Draw rainbow that uniformly distributes itself across all pixels."""
        for j in range(256*iterations):
            for i in range(ledCount):
                self.strip.setPixelColor(
                    i, self.__wheel((int(i * 256 / ledCount) + j) & 255))
            self.strip.show()
            sleep(wait_ms/1000.0)

    def __rainbowCycleOne(self, strip, ledNo, wait_ms=2, iterations=3):
        """Draw rainbow on one pixel."""
        for j in range(256*iterations):
            self.strip.setPixelColor(
                ledNo - 1, self.__wheel((int(ledNo * 256) + j) & 255))
            self.strip.show()
            sleep(wait_ms/1000.0)

    def __blank(self, strip):
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, Color(0, 0, 0))
        self.strip.show()
