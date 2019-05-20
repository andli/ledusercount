#!/usr/bin/env python3

import urllib.request
import urllib.error
import discord
import asyncio
from math import *
from time import sleep
import logging

# Select your module here by uncommenting the correct one.
# Make sure to have used the corresponding provisioning script.
from modules import stdout as if_module
#from modules import blinkstick as if_module
#from modules import ws281x as if_module

interface_module = if_module.bot_interface_module()

logger = logging.getLogger('discord')
logger.setLevel(logging.WARNING)
handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()
userCount = 0


def wait_for_internet_connection():
    while True:
        try:
            response = urllib.request.urlopen('https://www.google.com')
            # print(response)
            return
        except urllib.error.URLError as e:
            print(e.reason)
            pass


@client.event
async def on_ready():
    countAndShowLeds()


@client.event
async def on_voice_state_update(member, before, after):
    countAndShowLeds()


def countAndShowLeds():
    global userCount
    oldUserCount = userCount
    userCount = 0

    for channel in client.get_all_channels():
        if channel.name != 'AFK':
            if channel._type == discord.ChannelType.voice.value:
                userCount += len(channel.members)

    interface_module.updateLeds(userCount, oldUserCount)


# Main program logic follows:
if __name__ == '__main__':
    wait_for_internet_connection()

    apikey = open('apikey.txt').read().rstrip()
    client.run(apikey)
