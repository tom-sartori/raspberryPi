# Manuel d'utilisation de l'Ultra dej 3000 
## Réalisé par SARTORI Tom et TEENA Nuihau



## Table des matières

1. [Ultra dej 3000](#introduction)
1. [Installation](#installation)
1. [Utilisation](#utilisation)
1. [Librairies](#librairies)
1. [Dweet](#dweet)



## 1. Ultra dej 3000 <a name=introduction></a>

### Le préparateur autonome de petit déjeuner 

Au réveil, vous avez besoin d’un bon remontant pour bien débuter votre journée. Hélas, il se trouve que vous n’avez pas toujours le temps de bien préparer votre petit déjeuner. Pas de soucis, notre produit est là pour vous simplifier dans cette tâche. Vous pourrez laisser le Ultra dej 3000 préparer votre petit déjeuner pendant que vous vous préparez. En effet, il suffit de sélectionner la quantité de céréales et de lait et grâce à un système de balance et de moteur, la machine prélève ce dont vous avez besoin. 


## 2. Installation <a name=installation></a>

### Capteurs nécessaires 

- 3 Boutons (gauche/droite/valider)
- Led 
- Ecran LCD
- Relay 
- Pompe à liquide et alimentation
- Balance
- Servomoteur


### Table des ports

| Capteur           | Port      |
| :---:             | :---:     |
| Bouton gauche     | D2        |
| Bouton central    | D3        |
| Bouton droit      | D4        |
| LED               | D5        |
| LCD               | I2C-3     |
| Relay             | D6        |

| Capteur   | Cable     | Pin number    | Pin name          |
| :---:     | :---:     | :---:         | :---:             |
| Balance   | Rouge     | 02            | DC Power 5v       |
| Balance   | Noir      | 06            | Ground            |
| Balance   | Blanc     | 11            | GPIO 17           |
| Balance   | Jaune     | 13            | GPIO 27           |
| Servo     | Rouge     | 17            | DC Power 3.3v     |
| Servo     | Brun      | 25            | Ground            |
| Servo     | Orange    | 15            | GPIO 22           |


### Installation de la pompe 

La pompe fait partie d'un circuit fermé avec le relay et l'alimentation (les piles). 
Le relay permet de faire passer, ou non le courant et ainsi, alumer ou non la pompe. 

Pour le branchement, il faut : 
- Connecter un cable du relay à l'alimentation. 
- Connecter l'autre cable de l'alimentation avec un de la pompe. 
- Connecter le dernier cable de la pompe vers le port restant du relay. 

N.B. : Si la pompe ne fonctionne pas, il faut échanger les cables au niveau du relay. 



## 3. Utilisation <a name=utilisation></a>

### Lancement du programme au démarrage

Lors du démarrage de la raspberry, le programme principale devrait ce lancer. Pour modifier ce paramétrage, il faut modifier le fichier crontab avec la commmande suivante. 
```shell script
sudo crontab -e
```


### Lancement manuel et modification du programme

Le programme principal et les librairies sont contenues sur la raspberry. Pour y accéder, il est possible de connecter la rap à un écran, ou d'accéder aux fichier via ssh. 

Les codes sources Python sont contenus dans le dossier suivant : `/home/pi/Documents/lib/`. Ils sont également disponibles sur ce [lien gitHub](https://github.com/tom-sartori/raspberryPi/tree/master/src/lib). 

Le programme principal (qui se lance au démarrage) est `main.py`. 



### 4. Librairies <a name=librairies></a>

L'ensemble du code source des libriries a été préalablement téléchargé et est disponible dans le dossier suivant : `/home/pi/Documents/lib/`. 

La librairie `RPi.GPIO` doit cependant être installée sur la raspberry. 



### 5. Dweet <a name=dweet></a>

Lors de chaque utlisation du programme, des données sont récupérées. Ces dernières sont la quantité de céréales et de lait que l'utilisateur choisit. 

Ces données sont envoyées sur ce [lien Dweet](https://dweet.io/follow/unusual-shock), puis analysées sur ce [lien google sheet](https://docs.google.com/spreadsheets/d/1FXYH4dfClcvq0l42-L5FMeVME-BodEvl1K-2ylqNrUk/edit#gid=1870643192). 



