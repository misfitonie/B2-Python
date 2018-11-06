
#! D:\Python\python.exe
# 1d-mol
# jeu +/-
# FERREIRA Théo
# 06/11/2018

import random
import re
import signal

regexnb = re.compile("[0-9]+")
nbRandom = random.randint(0, 100)
nbTry = 0


def nepasquitter(signum, frame):
        print("\n Non ")


def nepasquitterdutout(signum, frame):
        print("\n STOP")


def Quitter():
    return print("\nLa solution était:", nbRandom)

signal.signal(signal.SIGINT, nepasquitter)
signal.signal(signal.SIGTERM, nepasquitterdutout)

while True:

    choixUser = input("Choisissez un nombre entre 0 et 100\n")

    if str(choixUser) == "q":
        Quitter()
        break

    if int(choixUser) < nbRandom:
        print("C'est plus grand")
        nbTry = nbTry + 1
        continue

    if int(choixUser) > nbRandom:
        print("C'est plus petit")
        nbTry = nbTry + 1
        continue

    if int(choixUser) == nbRandom:
        print("Bravo tu as trouvé en "+str(nbTry)+" tentatives !")
        break
