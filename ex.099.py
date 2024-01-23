#função pra analisar todos os valores e dizer qual deles é o maior
from time import sleep
def maior( * num):
    maior = cont = 0
    print('-'*30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'[{valor}]', end='', flush = True)
        sleep(0.3)
        
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont+=1
    print(f'\nForam informados {cont} ao todo.')
    print(f'O maior deles é {maior}.')
maior(1,1.5)
maior(99,100,4,2)
maior(2,7,5,10,55)
maior(1,2,3,4,5) 
input()