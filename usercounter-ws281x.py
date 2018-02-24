# sudo apt install python3-pip -y
# sudo apt-get install build-essential python-dev git scons swig
# git clone https://github.com/jgarff/rpi_ws281x.git
# cd rpi_ws281x
# scons
# cd python
# sudo python3 setup.py install
# sudo python3 -m pip install discord.py

import discord
import asyncio
from math import *
from time import sleep
import logging
from neopixel import *

# LED strip configuration:
LED_COUNT	  = 8	  # Number of LED pixels.
LED_PIN		= 18	  # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN		= 10	  # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ	= 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA		= 10	  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 100	 # Set to 0 for darkest and 255 for brightest
LED_INVERT	 = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL	= 0	   # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP	  = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

logger = logging.getLogger('discord')
logger.setLevel(logging.WARNING)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

strip = None
client = discord.Client()
defaultColor = Color(18,18,18)
userCount = 0


@client.event
async def on_ready():
	countAndShowLeds()


@client.event
async def on_voice_state_update(before, after):
	countAndShowLeds()


def pulseTopSubset(lowerLimit, upperLimit):
	radsArray = []
	repetitions = 3
	fracs = 20
	for fraction in range(fracs):
		radsArray.append([pi * fraction / fracs])
	radsArray.append([0, 0, 0])

	for i in range(repetitions):
		for angle in radsArray:
			x = floor(sin(angle) * 255)
			ledData = []
			if lowerLimit > 0:
				for i in range(lowerLimit):
					ledData.append(defaultColor)
			for i in range(lowerLimit, upperLimit + 1):
				ledData.append([0, 0, x])
			if upperLimit < 7:
				for i in range(upperLimit + 2, 8):
					ledData.append([0, 0, 0])
			bstick.set_led_data(channel=0, data=ledData)
			sleep(0.05)


def setLedRange(strip, min, max):
	ledData = []
	for i in range(min):
		ledData.append(Color(0, 0, 0))
	for i in range(min, max + 1):
		ledData.append(defaultColor)
	pos = 0
	for j in ledData:
		strip.setPixelColor(pos, j)
		pos += 1
	strip.show()


def setIndividualLed(ledNo, colorHex):
	ledData = []
	for i in range(7 + 1):
		ledData.append([0, 0, 0])
	ledData[ledNo * 3:ledNo * 3 + 3] = colorHex
	bstick.set_led_data(channel=0, data=ledData)


def countAndShowLeds():
	global userCount
	oldUserCount = userCount
	userCount = 0

	for channel in client.get_all_channels():
		if channel.name != 'AFK':
			userCount += len(channel.voice_members)

	#print(userCount)

	if strip is not None:
		#rainbowCycle(strip)
		blank(strip)
		if userCount > oldUserCount:
			if oldUserCount > 0:
				setLedRange(strip, 0, oldUserCount - 1)
			#pulseTopSubset(oldUserCount, userCount - 1)
		setLedRange(strip, 0, userCount - 1)

		#if userCount == 0:
		#	setIndividualLed(7, [18, 0, 0])

			
def wheel(pos):
		"""Generate rainbow colors across 0-255 positions."""
		if pos < 85:
				return Color(pos * 3, 255 - pos * 3, 0)
		elif pos < 170:
				pos -= 85
				return Color(255 - pos * 3, 0, pos * 3)
		else:
				pos -= 170
				return Color(0, pos * 3, 255 - pos * 3)

				
def rainbowCycle(strip, wait_ms=2, iterations=5):
		"""Draw rainbow that uniformly distributes itself across all pixels."""
		for j in range(256*iterations):
				for i in range(strip.numPixels()):
						strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
				strip.show()
				sleep(wait_ms/1000.0)

def blank(strip):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, Color(0,0,0))
	strip.show()
				
# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions)
	strip.begin()
	
	apikey = open('apikey.txt').read().rstrip()
	client.run(apikey)
