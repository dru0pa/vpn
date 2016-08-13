#!/bin/bash

# This script looks for data in the file /tmp/openvpn/step3.txt
# This is so that the the counter can be incrmented.

# Writen by Andrew Price dru0pa@gmail.com

if [ -s /home/pi/tmp/openvpn/step3.txt ]
	then
		echo "File has data."
	else
		echo "File has no data."
		echo "NODATA" > /home/pi/tmp/openvpn/step3.txt
fi
