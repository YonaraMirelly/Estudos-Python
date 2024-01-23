from time import sleep
#função
def contador(i,f,p):
    if p < 0:
        p*= -1
    if p == 0:
        p = 1
    print('-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(2)
    
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end = '', flush=True)
            sleep(0.5)
            cont += p
        print(' :) ')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end = '', flush =True)
            sleep(0.5)
            cont -=p
        print(' :) ')
#contador principal
contador(1,10,1)
contador(10,0,2)
print('-='*20)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início:  '))
fim = int(input('Fim:     '))
passo = int(input('Passo: '))
contador(ini, fim, passo)
input()