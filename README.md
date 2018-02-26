# ledusercount

Using a WS2812 5050 RGB LED this Discord bot shows how many of your friends are logged in to your Discord server.

* Shows a green LED up top when the bot is online but noone is logged in.
* Excludes the channel ```AFK``` when counting users.

#### Prerequisites
* Python 3.4+
* Pip

```
TBD
```

#### Running it
Set up a Discord bot
Add your Discord bot token to a text file called apikey.txt in the repo.
```
python3 usercounter.py &
```
or add an `@reboot` line to crontab:
```
sudo /usr/bin/python3 /home/pi/usercounter/usercounter-ws281x.py > /home/pi/cronjoblog 2>&1
```
