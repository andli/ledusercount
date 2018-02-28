# ledusercount

Using a WS2812 5050 RGB LED this Discord bot shows how many of your friends are logged in to your Discord server.

[Imgur](https://i.imgur.com/EIKJVU9m.jpg)

* Shows a red LED up top when the bot is online but noone is logged in.
* Excludes the channel ```AFK``` when counting users.
* Shows up to the maximum number of leds of the attached led strip.

#### Prerequisites
* Python 3.4+
* Pip

```
sudo apt install python3-pip -y
sudo apt-get install build-essential python-dev git scons swig
git clone https://github.com/jgarff/rpi_ws281x.git
cd rpi_ws281x
scons
cd python
sudo python3 setup.py install
sudo python3 -m pip install discord.py
```

#### Running it
Set up a Discord bot (Google for instructions if you don't know how).
Add your Discord bot token to a text file called apikey.txt in the repo.
```
python3 usercounter.py &
```
or add an `@reboot` line to crontab:
```
sudo /usr/bin/python3 /home/pi/usercounter/usercounter-ws281x.py > /home/pi/cronjoblog 2>&1
```
