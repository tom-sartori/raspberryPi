# coding: utf-8
import smbus
import time
import random

bus = smbus.SMBus(1)  # pour I2C-1 (0 pour I2C-0)

# Indiquez ici les deux adresses de l'ecran LCD
# celle pour les couleurs du fond d'ecran 
# et celle pour afficher des caracteres
DISPLAY_RGB_ADDR = 0x62
DISPLAY_TEXT_ADDR = 0x3e

########################################################################################################################
# Partie couleur de fond.

color = {
    'red': [255, 0, 0],
    'green': [0, 255, 0],
    'blue': [0, 0, 255],
    'white': [255, 255, 255],
    'magenta': [255, 0, 255],
    'black': [0, 0, 0]
}


# Permet de choisir la couleur de fond de l'écran.
# 0 <= rouge, vert, bleu <= 255
def setRGB(rouge, vert, bleu):
    bus.write_byte_data(DISPLAY_RGB_ADDR, 0x00, 0x00)
    bus.write_byte_data(DISPLAY_RGB_ADDR, 0x01, 0x00)
    bus.write_byte_data(DISPLAY_RGB_ADDR, 0x02, bleu)
    bus.write_byte_data(DISPLAY_RGB_ADDR, 0x03, vert)
    bus.write_byte_data(DISPLAY_RGB_ADDR, 0x04, rouge)
    bus.write_byte_data(DISPLAY_RGB_ADDR, 0x08, 0xAA)


# Permet de choisir la couleur de fond de l'écran.
# colorDico est une couleur dans le dico color.
def setColor(colorDico):
    setRGB(colorDico[0], colorDico[1], colorDico[2])


########################################################################################################################
# Partie text

LINE_SIZE = 16


# Envoie  a l'ecran une commande concerant l'affichage des caracteres.
# cmd est de type hexa.
def textCmd(cmd):
    bus.write_byte_data(DISPLAY_TEXT_ADDR, 0x80, cmd)
    time.sleep(0.001)


# Initialise l'affichage.
def clearText():
    textCmd(0x01)  # clear display                  sudo i2cset -y 1 0x3e 0x80 0x01
    textCmd(0x0F)  # display on, block cursor       sudo i2cset -y 1 0x3e 0x80 0x0F
    textCmd(0x38)  # 2 lines                        sudo i2cset -y 1 0x3e 0x80 0x38


# Fait un retour chariot.
def lineBreak():
    textCmd(0xc0)


# Affiche le caractère en param.
# char est un caractère alpha numérique.
def setChar(char):
    bus.write_byte_data(DISPLAY_TEXT_ADDR, 0x40, ord(char))


# Completez le code de la fonction permettant d'ecrire le texte recu en parametre
# Si le texte contient un \n ou plus de 16 caracteres pensez a gerer
# le retour a la ligne
# def setText16(texte):
#     clearText()
#
#     for i in range(len(texte)):
#         if i == 16 or texte[i] == '\n':
#             textCmd(0xc0)
#         # time.sleep(0.05)
#         setChar(texte[i])


# Affiche une ligne de 16 caractères maximum.
def setLine(line):
    for i in range(len(line)):
        setChar(line[i])


def setLineHuman(line):
    for i in range(len(line)):
        if line[i] != ' ':
            time.sleep(random.uniform(0.01, 0.5))
        setChar(line[i])


# Affiche le texte en le faisant défiler en haut en bas.
def setText(text):
    sleepTime = 1

    newText = ' ' * LINE_SIZE  # en bas
    # oldText en haut

    i = 0
    while len(newText) == LINE_SIZE:
        clearText()
        oldText = newText

        if text[i] == ' ':
            i += 1

        if i + LINE_SIZE > len(text):
            newText = text[i:]
        else:
            newText = text[i: i + LINE_SIZE]
            i += LINE_SIZE

        newText = getAsciiText(newText)

        print('old : ' + oldText)
        print('new : ' + newText)
        print('\n')

        setLine(oldText)
        lineBreak()
        setLineHuman(newText)
        time.sleep(sleepTime)

    clearText()
    setLine(newText)
    time.sleep(sleepTime)

    clearText()

    #
    #
    # for i in range(0, len(text), LINE_SIZE * 2):
    #     setLine(text[i: i + LINE_SIZE])
    #     lineBreak()
    #     time.sleep(1)
    #     setLine(text[i: i + LINE_SIZE])
    #     lineBreak()
    #     time.sleep(1)
    #     #
    #     # if i % 32 == 0:
    #     #     textCmd(0x01)
    #     # elif i % 16 == 0 or text[i] == '\n':
    #     #     lineBreak()
    #     #     time.sleep(2)
    #     # setChar(text[i])


# Affiche le texte en param en le faisant défiler de droite à gauche.
def setTextDefile(text):
    sleepTime = 0.15
    text = getAsciiText(text)

    for i in range(LINE_SIZE):
        time.sleep(sleepTime)
        clearText()
        setLine(' ' * (LINE_SIZE - i) + text[:i])

    for i in range(len(text) + 1):
        time.sleep(sleepTime)
        clearText()
        setLine(text[i: i + LINE_SIZE])


# Demande un texte à l'utilisateur et l'affiche.
def setTextInput():
    text = input('Texte à afficher : ')
    setText(text)


# Demande un texte à l'utilisateur et l'affiche en le faisant défiler de gauche à droite.
def setTextInputDefile():
    text = input('Texte à afficher : ')
    setTextDefile(text)


def getAsciiText(text):
    text = text.replace('é', 'e')
    text = text.replace('è', 'e')
    text = text.replace('à', 'a')
    text = text.replace('ç', 'c')

    return text
