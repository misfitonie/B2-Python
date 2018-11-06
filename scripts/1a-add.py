#! D:\Python\python.exe
# 1a-add
# addition 2 nombres
# FERREIRA Théo
# 06/11/2018

#fonction vérification d'entrer de chiffre
def convertInt(param):
    try:
        return int(param)
    except ValueError:
        print("Vous n'avez pas entré un nombre !")
        exit()
        
  #entrer du nombre 1
nb1 = convertInt(input('Veuillez entrer un nombre.\n'))

  #entrer du nombre 2
nb2 = convertInt(input('Veuillez un second nombre.\n'))

  #fonction d'addition 
print("Voilà le résultat : " + str(nb1 + nb2))
