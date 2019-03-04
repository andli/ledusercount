#!/usr/bin/env bash

apt update -y
apt upgrade -y

sudo apt install git python3-pip scons -y

#sudo apt-get install build-essential python-dev swig
git clone https://github.com/jgarff/rpi_ws281x.git

cd rpi_ws281x
scons
cd python
sudo python3 setup.py install
cd /home/pi/ledusercount
pip3 install -r requirements.txt

