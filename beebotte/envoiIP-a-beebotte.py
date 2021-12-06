# Soucis  de ce systeme : il faut s'identifier pour avoir 
# les resultats sinon faire tourner sur une autre machine 
# un script python qui lit les dernieres ip publiees


#Include the Beebotte SDK for Python
from beebotte import *
import socket
import time

# Waits for 20s 
#(enough time for the computer to get an ip address at boot)
time.sleep(20)



# Compte Beebotte : ig3 / ig3.yopmail.com
API_KEY  = "enEx5s6W1HkD7tR3U5F4HvTI"
SECRET_KEY = "YRaj7Ar2HHkpldnUcC4TVYIPNyyWJgi5"

bclient = BBT(API_KEY, SECRET_KEY)


# Recupere le nom de la machine
hostname = socket.gethostname()
# Recupere l'adresse ip
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
adresse_ip = s.getsockname()[0]
msg=hostname+' '+adresse_ip
#print(s.getsockname()[0])


## Create a Resource object indicating a "channel" name and a "resource": 
res1 = Resource(bclient, 'channel_IP', 'ip')

## Write to the resource
res1.write(msg)
## Or simply
#bclient.write('dev', 'res1', 'Hello World')

