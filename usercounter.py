# sudo apt install python3-pip -y
# sudo pip install pyusb==1.0.0b1
# sudo pip install blinkstick
# sudo blinkstick --add-udev-rule
# pip3 install blinkstick discord

import discord
import asyncio
#from blinkstick import blinkstick
from math import *
from time import sleep
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.WARNING)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bstick = None
#bstick = blinkstick.find_first()
#bstick.turn_off()
client = discord.Client()
defaultColor = [18,18,18]
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
        radsArray.extend([pi * fraction / fracs])
    radsArray.extend([0, 0, 0])

    for i in range(repetitions):
        for angle in radsArray:
            x = floor(sin(angle) * 255)
            ledData = []
            if lowerLimit > 0:
                for i in range(lowerLimit):
                    ledData.extend(defaultColor)
            for i in range(lowerLimit, upperLimit + 1):
                ledData.extend([0, 0, x])
            if upperLimit < 7:
                for i in range(upperLimit + 2, 8):
                    ledData.extend([0, 0, 0])
            bstick.set_led_data(channel=0, data=ledData)
            sleep(0.05)


def setLedRange(min, max):
    ledData = []
    for i in range(min):
        ledData.extend([0, 0, 0])
    for i in range(min, max + 1):
        ledData.extend(defaultColor)
    bstick.set_led_data(channel=0, data=ledData)


def setIndividualLed(ledNo, colorHex):
    ledData = []
    for i in range(7 + 1):
        ledData.extend([0, 0, 0])
    ledData[ledNo * 3:ledNo * 3 + 3] = colorHex
    bstick.set_led_data(channel=0, data=ledData)


def countAndShowLeds():
    global userCount
    oldUserCount = userCount
    userCount = 0

    for channel in client.get_all_channels():
        if channel.name != 'AFK':
            userCount += len(channel.voice_members)

    print(userCount)

    if bstick is not None:
        bstick.turn_off()
        if userCount > oldUserCount:
            if oldUserCount > 0:
                setLedRange(0, oldUserCount - 1)
            pulseTopSubset(oldUserCount, userCount - 1)
        setLedRange(0, userCount - 1)

        if userCount == 0:
            setIndividualLed(7, [18, 0, 0])


client.run('REDACTED')
