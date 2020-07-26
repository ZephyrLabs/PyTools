#!/bin/bash 

### v1.1 ###

### Check user is root ###
if (( $EUID != 0 )); then
  echo "Please run as root"
  exit
fi

echo "Initializing the conversion, This might take a while... till then sit back and relax, we have you covered :)"
sleep 3
### Install needed packages ###
apt-get update
apt-get install -y dirmngr

### Add the Kali Linux GPG keys to aptitude ###
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ED444FF07D8D0BF6

### Replace the Debian repos with Kali repos ###
mv /etc/apt/sources.list /etc/apt/sources.list.debian
cat <<EOF > /etc/apt/sources.list
deb http://http.kali.org/kali kali-rolling main non-free contrib
# deb-src http://http.kali.org/kali kali-rolling main non-free contrib
EOF

### Update and install base packages ###
apt-get update
apt-get -y upgrade
apt-get -y dist-upgrade
apt-get -y autoremove --purge
apt-get -y install kali-linux

### Cleaning up ###
apt-get -y autoremove --purge
apt-get clean

### some dependencies.. ###
apt install libgcc-8-dev

### Kali linux tools ###
apt install kali-linux-default

### Kali linux desktop ###
apt install kali-desktop-xfce

### let's remove anything else that is not required ###
apt-get -y autoremove --purge
apt-get clean

### clean the terminal ###
clear
echo "all done."

### finishing it all up ###
echo -e "please reboot the system, would you like it now ? [Y/N]"
read $c

if (( $c == "Y" | $c == "y" )); then
  echo "restarting the system"
  sleep 3
  reboot now
fi







