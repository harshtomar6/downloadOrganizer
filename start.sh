#!/bin/sh

DIR="$(find /home/$USER/ -name 'downloadOrganizer.py')"
echo "@reboot nohup python3 ${DIR}" >> start

crontab -u $USER start
nohup python3 $DIR &

pwd
