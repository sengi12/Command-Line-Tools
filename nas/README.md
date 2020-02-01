# Raspberry Pi Nextcloud Server

Credit: https://pimylifeup.com/raspberry-pi-nextcloud-server/

> Dear Reader,
>
> My 2 cents: You can purchase a pre-configured NAS (Network Attached Storage) if you really want, but where's the fun in that? They also get very expensive very quickly and normally can take up a lot of unnecessary space. I prefer to go with the DIY approach to these sort of things, because they're cheaper and you learn a lot along the way. 
>
> The other cool feature of this approach is that it is extendable. If you have a single TB HDD all setup and realize you could use more space after some use, you can very easily get another larger HDD and set it up. If you'd like more storage with your NAS, you will have to buy a whole new one and as I said before that can be expensive.

---

## Setup and Installation Instructions

### Equipment:

#### Recommended

- [Raspberry Pi](https://go.pimylifeup.com/l8KF94/amazon/raspberrypi) 2 or 3
-  [Micro SD Card](https://go.pimylifeup.com/DUVENo/amazon/microsdcard) or a [SD card](https://go.pimylifeup.com/LmAkjt/amazon/sdcard) if you’re using an old version of the Pi.
-  [Power Supply](https://go.pimylifeup.com/TwjJnF/amazon/powersupply)
-  [Ethernet Cord](https://go.pimylifeup.com/9YIU76/amazon/ethernetcord) or [Wifi dongle](https://go.pimylifeup.com/89vmLk/amazon/wifidongle) (Pi 3 has WiFi inbuilt)
-  [External Hard drive](https://go.pimylifeup.com/veUYLn/amazon/externalharddrive) or [USB Drive](https://go.pimylifeup.com/rup0t8/amazon/usbthumbdrive)

#### Optional

-  [Raspberry Pi Case](https://go.pimylifeup.com/vbWKKX/allraspberrypicases)
-  [USB Keyboard](https://go.pimylifeup.com/FiheVF/amazon/usbkeyboard)
-  [USB Mouse](https://go.pimylifeup.com/2VE9AD/amazon/usbmouse)

### Installing Apache and PHP

1. First things first, let's update our package repositories:

```bash
sudo apt-get update
sudo apt-get upgrade
```

2. Let's install apache:

```bash
sudo apt-get install apache2
```

To verify that this apache server is up and running, just enter your Raspberry Pi's local IP address into any internet browser connected to the same internet connection. You can check you Pi's local IP a few different ways:

```bash
ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eth0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast state DOWN group default qlen 1000
    link/ether b8:27:eb:17:4b:5b brd ff:ff:ff:ff:ff:ff
3: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether b8:27:eb:42:1e:0e brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.143/24 brd 192.168.1.255 scope global wlan0
       valid_lft forever preferred_lft forever
    inet6 2600:1700:4280:2940::26/128 scope global noprefixroute dynamic
       valid_lft 2126sec preferred_lft 2126sec
    inet6 2600:1700:4280:2940:61fe:8725:b2e8:3641/64 scope global mngtmpaddr noprefixroute dynamic
       valid_lft 3135sec preferred_lft 3135sec
    inet6 fe80::15c9:85b8:9789:5c1c/64 scope link
       valid_lft forever preferred_lft forever
```

This is generally what I use as it will actually show you all of the active network adapters for the device. The address we want in this example is the `inet` pertaining to `wlan0`. In this example it is `192.168.1.143`. (Yours will differ, so replace my IP with yours wherever you see it)

3. Now we want to install PHP7.3 along with several relevant packages:

```bash
sudo apt-get install php7.3 php7.3-gd sqlite php7.3-sqlite3 php7.3-curl php7.3-zip php7.3-xml php7.3-mbstring
```

4. Now that we have all of the packages we need, we need to restart the apache2 server. Keep this command in mind as it may come in handy if your server starts acting weird on you:

```bash
sudo service apache2 restart
```

### Installing Nextcloud

1. Let's get to our workspace in our PI's html folder:

```bash
cd /var/www/html
```

2. Now we want to download the latest nextcloud release from their website and extract it into this html directory.

```bash
curl https://download.nextcloud.com/server/releases/nextcloud-16.0.3.tar.bz2 | sudo tar -jxv
```

3. In order for nextcloud to be built properly, we need to create a data folder for it to operate in:

```bash
sudo mkdir -p /var/www/html/nextcloud/data
```

4. Let's give this nextcloud folder the correct user user and group:

```bash
sudo chown -R www-data:www-data /var/www/html/nextcloud/
```

5. Let's also give it the right permissions:

```bash
sudo chmod 750 /var/www/html/nextcloud/data
```

6. Now that this is setup we should be able to check out our nextcloud server online at 

   `[your IP address]/nextcloud`

Mine is shown below for clarity:

```
192.168.1.143/nextcloud
```

7. Since this is the first time you will be visiting this site, you will be prompted to "Create an admin account". This is where you will choose your username and password for nextcloud server access.

   Click through all of the setup prompts. Once you've clicked through, you will be greeted by the nextcloud interface you can now use to see all your files.

### Moving Nextcloud's data folder

First thing we need to do with our working nextcloud server is to move the data directory so it doesn't just take up storage on our Raspberry PI's SIM card. Now the following instructions simply move the directory to a better location, we will mount the HDD to this new location afterwards.

1. let's make our new directory where we will store our data files. This is where you will mount your hard drive. The instructions I used tell you that you can put this wherever you want and you can do that, but I was having trouble getting it to work so I'll show you where I put mine.

```bash
sudo mkdir -p /mnt/nextcloud
```

2. Now we have to move our current data folder to this new location

```bash
sudo mv -v /var/www/html/nextcloud/data /mnt/nextcloud/data
```

3. Now we need to edit our nextcloud config file to look at this new location:

```bash
cd /var/www/html/nextcloud/config
```

4. Before we make changes, let's be smart and make a backup in case we screw up

```bash
sudo cp -p config.php config.php.bk
```

5. Now we should edit `config.php` with the editor of your choice. By default `nano` and `vi` will already be installed on your Raspberry PI. `vim` and `emacs` are also great editors that are not installed by default.

   I recommend installing `vim` however, as it is a much more powerful editor and is built off of `vi`. To do this run `sudo apt-get install vim`

   Once installed you can run the following:

```bash
sudo vim config.php
```

6. Now we need to change the following line within the editor. To do this, first navigate to the line you wish to edit inside `vim`. Then click `i` to enter INSERT mode. Make your changes as noted below. Once finished press `ESC` followed by `:wq` which means WRITE and QUIT. 

   > If you ever make a mistake within vim and want to just quit without saving, press `ESC` like I mention above. And press `:q!` as this is a Force QUIT.

from:

```bash
'datadirectory' => '/var/www/html/nextcloud/data',
```

to:

```bash
'datadirectory' => '/mnt/nextcloud/data',
```

7. You should now be able to refresh the site and see all your files within that data folder.

...to be continued...

for now check out https://pimylifeup.com/raspberry-pi-nextcloud-server/ for a complete tutorial