#!/bin/sh

apt update -y
apt upgrade -y

pip install pyusb==1.0.0b1
pip install blinkstick
blinkstick --add-udev-rule