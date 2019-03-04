# ledusercount

Using a WS2812 5050 RGB LED this Discord bot shows how many of your friends are logged in to your Discord server.

Solder the LED strip to pin 18, +5V and GND respectively.

![The device in action](https://i.imgur.com/EIKJVU9m.jpg)

* Shows a red LED up top when the bot is online but noone is logged in.
* Flashes leds when a new user joins.
* Excludes the channel ```AFK``` when counting users.
* Shows up to the maximum number of leds of the attached led strip.

#### Provisioning
```
sudo ./provision.sh
```

#### Running it
Set up a Discord bot (Google for instructions if you don't know how).
Add your Discord bot token to a text file called apikey.txt in the repo.
```
python3 usercounter.py &
```
or add an `@reboot` line to crontab:
```
@reboot sudo /usr/bin/python3 /home/pi/ledusercounter/usercounter-ws281x.py > /home/pi/cronjoblog 2>&1
```
