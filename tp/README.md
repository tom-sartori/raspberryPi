ssh pi@ig-rasp05
sudo ifconfig
nmap -v -sn 162.38.110.36/24

sudo adduser sartori
raspberrytom
sudo visudo
su sartori 
ssh sartori@ig-rasp05

ssh-keygen -t rsa
ssh-copy-id sartori@ig-rasp05


who 
lastlog
w     Montre les dernières commandes


architecture : 
uname -m
armv7l

coeurs : 
cat /proc/cpuinfo 



Kill personne 
ps -ax
sudo kill -9  pid







TP2 

// Check tout ce qui a été fait depuis le boot. 
dmesg 

sudo apt-get aptitude install


sudo i2cdetect -y 1

sartori@ig-rasp01:/home/pi $ sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          03 04 -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- 3e -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- 62 -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: 70 -- -- -- -- -- -- --    

sartori@ig-rasp01:/home/pi $ sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- 04 -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- --                         




man i2cset

sudo i2cset -y 1 0x62 0x00 0x00 # mode 1 init, normal mode
sudo i2cset -y 1 0x62 0x01 0x00 # mode 2 init

sudo i2cset -y 1 0x62 0x02 0x00 # r
sudo i2cset -y 1 0x62 0x03 0xFF # g
sudo i2cset -y 1 0x62 0x04 0x00 # b
sudo i2cset -y 1 0x62 0x08 0xAA 



sudo i2cset -y 1 0x3e 0x80 0x01 # clear display
sudo i2cset -y 1 0x3e 0x80 0x0F # display on, block cursor 
sudo i2cset -y 1 0x3e 0x80 0x38 # 2 lines

i2cset -y 1 0x3e 0x40 80 # 80 acsii





Création ssh 

ssh pi@ig-rasp05
sudo ifconfig
nmap -v -sn 162.38.110.36/24

sudo adduser sartori
raspberrytom
sudovisudo
su sartori 
ssh sartori@ig-rasp05

ssh-keygen -t rsa
ssh-copy-id sartori@ig-rasp05





