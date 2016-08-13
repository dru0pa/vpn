#!/bin/bash

# This script is to start up the VPN on bootup
# This script need to added to the /etc/rc.local
# Need to run chmod +x /etc/rc.local to allow for exicution

# Writen by Andrew Price dru0pa@gmail.com

sleep 30
mkdir -p /tmp/openvpn
sleep 30
echo "$(date) The VPN is Going to connected to server after startup" >> /var/log/openvpn-scrit-log
python /etc/openvpn/Script-for-openvpn.py
