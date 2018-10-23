#! D:\Python\python.exe

def convertInt(param):
    try:
        return int(param)
    except ValueError:
        print("Vous n'avez pas entré un nombre !")
        exit() 

nb1 = convertInt(input('Veuillez entrer un nombre.\n'))
nb2 = convertInt(input('Veuillez un second nombre.\n'))

print("Voilà le résultat : " + str(nb1 + nb2))