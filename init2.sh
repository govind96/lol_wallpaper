#!/bin/bash

PID=$(pgrep mate-session)
export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)
wget https://raw.githubusercontent.com/govind96/lol_wallpaper/master/dank_wallpaper.py -P /home/user/Downloads
python /home/user/Downloads/dank_wallpaper.py
sleep 2
gsettings set org.mate.background picture-filename /home/user/.config/you_can_not_escape.png
rm /home/user/Downloads/dank_wallpaper*.py
sleep 5
#commenting now to see the effect
#rm /home/user/Pictures/you_can_not_escape.png
