#!/usr/bin/python
# This script it to radnomis the connection to different vpn servers.
# There are chnages needed to each ovpn file to allaow the access to the username and password
# /etc/openvpn/ipvanish-config.txt must contain the username and password olny (seperat lines)
# Add this to the file auth-user-pass /etc/openvpn/ipvanish-config.txt, replacing auth-user-pass

# Writen by Andrew Price dru0pa@gmail.com

import os

from random import randint



choice = randint(1,15)

if choice == 1:
	os.system ("sudo openvpn --config /etc/openvpn/ipvanish-US-San-Jose-sjc-a01.ovpn &")
elif choice == 2:
        os.system ("sudo openvpn --config /etc/openvpn/ipvanish-US-San-Jose-sjc-a02.ovpn &")
elif choice == 3:
        os.system ("sudo openvpn --config /etc/openvpn/ipvanish-US-San-Jose-sjc-a03.ovpn &")
elif choice == 4:
        os.system ("sudo openvpn --config /etc/openvpn/ipvanish-US-San-Jose-sjc-a04.ovpn &")
elif choice == 5:
        os.system ("sudo openvpn --config /etc/openvpn/ipvanish-US-San-Jose-sjc-a05.ovpn &")
elif choice == 6:
        os.system ("sudo openvpn --config /etc/openvpn/ipvanish-US-San-Jose-sjc-a06.ovpn &")
elif choice == 7:
        os.system ("sudo openvpn --config /etc/openvpn/ipvanish-US-San-Jose-sjc-a07.ovpn &")
elif choice == 8:
        os.system ("sudo openvpn --config /etc/openvpn/ipvanish-US-San-Jose-sjc-a08.ovpn &")
elif choice == 9:
        os.system ("sudo openvpn --config /etc/openvpn/ipvanish-US-San-Jose-sjc-a09.ovpn &")
elif choice == 10:
        os.system ("sudo openvpn --config /etc/openvpn/ipvanish-US-San-Jose-sjc-a10.ovpn &")
elif choice == 11:
        os.system ("sudo openvpn --config /etc/openvpn/ipvanish-US-San-Jose-sjc-a11.ovpn &")
elif choice == 12:
        os.system ("sudo openvpn --config /etc/openvpn/ipvanish-US-San-Jose-sjc-a12.ovpn &")
elif choice == 13:
        os.system ("sudo openvpn --config /etc/openvpn/ipvanish-US-San-Jose-sjc-a13.ovpn &")
elif choice == 14:
        os.system ("sudo openvpn --config /etc/openvpn/ipvanish-US-San-Jose-sjc-a14.ovpn &")
elif choice == 15:
        os.system ("sudo openvpn --config /etc/openvpn/ipvanish-US-San-Jose-sjc-a15.ovpn &")






