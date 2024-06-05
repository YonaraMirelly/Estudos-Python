from time import sleep
import os
vermelho = '\033[1;31mVERMELHO\033[m'
amarelo = '\033[1;33mAMARELO\033[m'
verde = '\033[1;32mVERDE\033[m'


def limpar():
    if os.name == 'nt':
        os.system('cls')

lista = [vermelho, amarelo, verde]

while True:
    for i in lista:
        limpar()
        print(i)
        sleep(4)
    
