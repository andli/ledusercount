#!/bin/sh

#add command to crontab if it is not already there
command="sudo /usr/bin/python3 /home/pi/ledusercount/usercounter.py > /home/pi/cronjoblog 2>&1"
crontab -l | fgrep -i -v "$command" | { cat; echo "$job"; } | crontab -