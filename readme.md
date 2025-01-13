# raspberry pi 4 wifi router

this is a guide to set up a raspberry pi 4 as a wifi router.


download the latest version of openwrt from [here](https://downloads.openwrt.org/releases/23.05.0/targets/armvirt/64/openwrt-23.05.0-armvirt-64-default-rootfs.tar.gz)

on mac use belina to flash the image to the sd card which can be found [here](https://www.balena.io/etcher/)

use a sub to ethernet cable to connect the pi to the internet. For exmple this can be 

 openwrt image builder [here](https://firmware-selector.openwrt.org/?version=23.05.5&target=bcm27xx%2Fbcm2711&id=rpi-4)

 and commant to add to build is here

 #clone this repo on build and dhcp and network config in /etc/config/

 #run the build script

 #copy the image to the sd card

 #boot the pi and connect to the wifi network

 

 ```bash
 git clone git@github.com:fdsig/openwrst-rp.git
 cd openwrt-rp
 cp ./dhcp /etc/config/dhcp
 cp ./network /etc/config/network
 ```

after shelling in run on any packges that have not been specified in the open-wrt-build. eg an ethernet cable to usb driver for TP-Link UE300 USB 3.0 to Gigabit Ethernet Adapter.

```bash
opkg update
opkg install kmod-usb-net-cdc-ether
```

