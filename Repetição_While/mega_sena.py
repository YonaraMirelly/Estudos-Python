from random import randint
from time import sleep
print('='*40)
print('          JOGO NA MEGA SENA          ')
print('='*40)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot  = 1
lista = []
jogos = []
while tot <= quant:
    cont = 0
    while True:
        num = randint(0,60)
        if num not in lista:
            lista.append(num)
            cont +=1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot +=1
print('-+'*5, f'SORTEANDO {quant} JOGOS', '-+'*5)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0.6)
print(';)')
input()