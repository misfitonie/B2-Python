#! D:\Python\python.exe
# 1d-dic
# entrer des noms et en faire une liste
# FERREIRA Théo
# 06/11/2018

import re
nom = input("Entez un nom : (Appuyer sur Q pour quitter)")

# la condition que l'on doit importé
pattern = re.compile("^[^0-9]+$")
listePrenom = []


# ajouter des noms à une liste puis les afficher
def ajouterPrenom(nom):
        while nom != "q":
            if (pattern.match(nom)):
                listePrenom.append(nom)
                nom = input("Entrez un nom, ou appuyer sur Q pour quitter : ")
            else:
                nom = input("Entrez un nom correct : ")

        listePrenom.sort()

# afficher la ligne des noms
        print('\nVoici la liste des noms :')
        for nom in listePrenom:
            print (nom)

ajouterPrenom(nom)

input("Appuyer sur une touche pour quitter.")
