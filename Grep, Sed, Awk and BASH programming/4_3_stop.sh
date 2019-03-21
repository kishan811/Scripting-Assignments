#!/bin/bash
sudo sed -i '1d' '/etc/resolv.conf'
sudo killall openvpn
