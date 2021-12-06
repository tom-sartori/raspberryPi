from beebotte import *

# Compte Beebotte : ig3 / ig3.yopmail.com
API_KEY  = "enEx5s6W1HkD7tR3U5F4HvTI"
SECRET_KEY = "YRaj7Ar2HHkpldnUcC4TVYIPNyyWJgi5"
bclient = BBT(API_KEY, SECRET_KEY)

## Create a Resource object indicating a "channel" name and a "resource": 
res1 = Resource(bclient, 'channel_IP', 'ip')
## Read from the resource
#records = res1.read(limit = 1, source = 'hour-stats')
## Do something with records (JSON format)

records = res1.read(limit = 10) # lit les 10 dernières valeurs publiées
for ligne in records:
	print(ligne['data'])
## Or simply
#records = bclient.read('dev', 'res1', limit = 24, source = 'hour-stats')

#print(records)
