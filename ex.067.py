from time import sleep
n = 0
opçao = ''
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-'*30)
    for i in range(0,11):
        print(f'{n} x {i} = {n*i}')
        sleep(0.75)
    print('-'*30)
    opçao = str(input('Quer continuar? [S/N] ')).upper()[0]
    if opçao in "N":
        break
print('-'*30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
input()