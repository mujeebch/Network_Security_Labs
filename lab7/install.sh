# lab 7 install script
# Nils, SUTD, 2015
sudo apt-get install -y kismet-plugins aircrack-ng
sudo add-apt-repository ppa:nilarimogard/webupd8
sudo apt-get update
sudo apt-get install -y ap-hotspot
# kismon install
sudo apt-get install -y git python3 python3-gi gir1.2-gtk-3.0 \
 gir1.2-gdkpixbuf-2.0 python3-cairo python3-simplejson \
 python-osmgpsmap gir1.2-osmgpsmap-1.0

git clone https://github.com/Kismon/kismon.git kismon
cd kismon
make
sudo make install
sudo ln -s $PWD/bin/kismon /usr/local/bin/

# configure kismet for mon0
echo 'ncsource=mon0' | sudo tee --append /etc/kismet/kismet.conf

cd /tmp
#wget http://archive.ubuntu.com/ubuntu/pool/universe/w/wpa/hostapd_1.0-3ubuntu2.1_amd64.deb
wget http://archive.ubuntu.com/ubuntu/pool/universe/w/wpa/hostapd_2.1-0ubuntu1.4_amd64.deb
sudo dpkg -i hostapd*.deb
sudo apt-mark hold hostapd
cd -
