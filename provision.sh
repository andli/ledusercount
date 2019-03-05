#!/bin/sh

apt update -y
apt upgrade -y

sudo apt install git python3-pip scons swig -y

#sudo apt-get install build-essential python-dev 
git clone https://github.com/jgarff/rpi_ws281x.git

cd rpi_ws281x
scons
cd python
sudo python3 setup.py install
cd /home/pi/ledusercount
pip3 install -r requirements.txt

command="sudo /usr/bin/python3 /home/pi/ledusercount/usercounter-ws281x.py > /home/pi/cronjoblog 2>&1"
job="@reboot $command"
crontab -l | fgrep -i -v "$command" | { cat; echo "$job"; } | crontab -l
