#!/usr/bin/env python3

class bot_interface_module:

    def __init__(self):
        pass
    
    def updateLeds(self, userCount, oldUserCount):
        if userCount != oldUserCount:
            print("Old userCount = {}, new userCount = {}".format(oldUserCount, userCount))