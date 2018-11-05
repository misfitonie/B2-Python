#! D:\Python\python.exe

import random
import re
import signal

signal.signal(signal.SIGINT, end_game)

def read_in_file():
  file = open("plusoumoins.txt", "r")
  msg = file.readline().strip()
  file.close()
  return msg

def message():
    write_in_file('Dommage ! C\étais', str(nbr))
    exit()

def end_game(sig, frame):
    write_in_file('Quel erreur')
    exit()   

def write_in_file(msg):
  file = open("plusoumoins.txt", "w")
  file.write(msg)
  file.close()
  
end = False
nbr = random.randint(0,100)

write_in_file('Veuillez choisir entre 0 et 100 : ')

while end is False :
    
    saisi = read_in_file()
      
    if re.match("^[0-9]+$", saisi):
        saisi = int(saisi)
        
        if saisi > 100:
            continue          
        if saisi > nbr :
            write_in_file('C\est moins !')       
        elif saisi < nbr :
            write_in_file('C\est plus !')
    
        else :
            write_in_file('Bravo ! ')
            end = True
            message()