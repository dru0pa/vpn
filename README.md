# VPN for openvpn

The VPN will do a connect to the vpn server and will check the connection to the server every 30 minutes.
Every time it starts up the VPN will do a random pick of one 16 VPN servers to connected to each time it needs to conneced.

This uses pyhton and bash. It just work not great yet still working on fixing some new problem new Rasbian


For systemd startup
Copy the file called vpnstart.service to /etc/systemd/system/ to adding the vpn to systemd startup
run thees comands
sudo chown root:root /etc/systemd/system/vpnstart.service
sudo chmod 755 /etc/systemd/system/vpnstart.service
sudo systemctl start vpnstart.service
sudo systemctl enable vpnstart.service



This Has NO garenty that it will work in any way or form. Use it is you like if not you chose not mine.

Add these line to your /etc/crontab

* 4 * * * root /etc/openvpn/Kill_OpenVpn.sh

0,30 * * * * root /etc/openvpn/Script-for-openvpn.py


Addd this line to openvpn config file for the vpn
auth-user-pass /etc/openvpn/ipvanish-config.txt
