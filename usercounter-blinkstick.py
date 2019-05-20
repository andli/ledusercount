#!/usr/bin/env python3

# sudo pip install pyusb==1.0.0b1
# sudo pip install blinkstick
# sudo blinkstick --add-udev-rule

import discord
import asyncio
import logging
import urllib.request

from modules import blinkstick

interface_module = blinkstick.blinkstick_module()

logger = logging.getLogger('discord')
logger.setLevel(logging.WARNING)
handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()
userCount = 0


@client.event
async def on_ready():
    countAndShowLeds()


@client.event
async def on_voice_state_update(before, after):
    countAndShowLeds()


def countAndShowLeds():
    global userCount
    oldUserCount = userCount
    userCount = 0
    for channel in client.get_all_channels():
        if channel.name != 'AFK':
            userCount += len(channel.voice_members)
    interface_module.updateLeds(userCount, oldUserCount)


def wait_for_net():
    while True:
        try:
            response = urllib.request.urlopen('https://www.google.com')
            return
        except urllib.error.URLError:
            pass


if __name__ == '__main__':
    wait_for_net()
    client.run('XXXXXXXXXXXXXXX')
