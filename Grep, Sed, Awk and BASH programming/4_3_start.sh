#!/bin/bash
sudo sed -i '1s/^/nameserver 10.4.20.204\n/' '/etc/resolv.conf'
read -p "Enter Username:" un
read -p  "Enter password:" pwd
wget --user $un --password $pwd http://vpn.iiit.ac.in/secure/ubuntu.ovpn
sudo apt install openvpn
# Change nobody to nogroup inside ovpn file(If Giving fatal error in linux.ovpn)
# sudo chgrp nogroup ./linux.ovpn
# sed -i -e 's/group nobody/group nogroup/' ./linux.ovpn
sudo openvpn --config ./ubuntu.ovpn
