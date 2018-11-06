#! D:\Python\python.exe
# 1c-moy
# entrer des notes pour un nom et faire moyenne
# FERREIRA Théo
# 06/11/2018

import operator


def convertInt(param):
    try:
        return int(param)
    except ValueError:
        return -1

dico = {}

print('Veuillez entrer un prénom et une note (séparés par un espace).')

while True:
    read = input('')

    if read == "q":
        break

    read = str(read).split(' ')

    if len(read) < 2:
        print("Je vous ai dit de mettre un espace !")
        continue

    nom = read[0]
    note = convertInt(read[1])

    if note == -1:
        print("Êtes-vous sûr d'avoir entré un nombre ?")
        continue

    if nom in dico:
        print("Vous avez déjà mis une note pour " + nom)
        continue

    dico[nom] = note

print(sorted(dico.items(), key=operator.itemgetter(1), reverse=True)[:5])
moy = sum(dico.values()) / len(dico)
print("La moyenne est de " + str(moy))
