# Usercounter

Using a Blinkstick usb LED device this Discord bot shows how many of your friends are logged in to your Discord server.

* Shows a green LED up top when the bot is online but noone is logged in.
* Excludes the channel ```AFK``` when counting users.

#### Prerequisites
* Python 3.4+
* Pip

```
sudo pip install pyusb==1.0.0b1
sudo pip install blinkstick
sudo blinkstick --add-udev-rule
pip3 install blinkstick discord
```

#### Running it
Add your Discord bot token to the appropriate place in the bottom of the file.
```
python3 usercounter.py &
```