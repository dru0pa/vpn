#!/usr/bin/python

# This script is to outomate the openvpn connection to conneced to multypl servers one at a time.
# This is to maintain a connection to vpn service with out being dependant on one server.
# This need to be added to the crontab
# 0,30 * * * * /etc/openvpn/Script-for-openvpn.py

# Writen by Andrew Price dru0pa@gmail.com

import os
import mmap

os.system ('sudo chmod -777 /home/pi/tmp/openvpn/ -R')


print ('Checking for prossess using grep')
os.system ('sudo ps aux | grep openvpn > /home/pi/tmp/openvpn/step1.txt')
os.system ('sudo cat /home/pi/tmp/openvpn/step1.txt | grep ipvanish> /home/pi/tmp/openvpn/step2.txt')
os.system ("sudo grep -v '^$' /home/pi/tmp/openvpn/step2.txt > /home/pi/tmp/openvpn/step3.txt")

print ('Looking for openvpn')

os.system ('sudo /etc/openvpn/Check-step2-for-data.sh')

a = open ('/home/pi/tmp/openvpn/step3.txt')
s = mmap.mmap(a.fileno(),0,access=mmap.ACCESS_READ)
if s.find('ipvanish')!= -1:
	print 'VPN is Connected'
	os.system ('echo "$(date) The VPN is connected to server" >> /var/log/openvpn-scrit-log')
else:
	print 'VPN is Not Connected'
	os.system ('echo "$(date) The VPN is NOT connected to server" >> /var/log/openvpn-scrit-log')
	print 'Starting VPN'
	os.system ('echo "$(date) The VPN connection is going to be started" >> /var/log/openvpn-scrit-log')
	os.system ('sudo python /etc/openvpn/Openvpn-Randome.py')
	os.system ('echo "$(date) The VPN is NOW connected to server" >> /var/log/openvpn-scrit-log')

os.system ('sleep 20') 
#os.system ('sudo service shorewall restart')
#os.system ('sudo systemctl start shorewall.service')
os.system ('sudo shorewall stop')
os.system ('sudo shorewall start')
