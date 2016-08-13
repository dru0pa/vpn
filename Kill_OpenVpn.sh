#!/bin/bash

# This script is to kill open vpn process
# This need to be added to the crontab
# * 4 * * * /etc/openvpn/Kill_OpenVpn.sh

# Writen by Andrew Price dru0pa@gmail.com

#ps aux | grep openvpn
sudo killall -p openvpn

echo "$(date) Kill all openvpn process" >> /var/log/openvpn-scrit-log

sudo systemctl stop shorewall.service

sudo rm -rf /home/pi/tmp/openvpn/

# sudo reboot
