#melhoria do ex.61
print('GERADOR DE PA')
print('-=' * 20)
pt = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
termo = pt
cont = 1
total = 0
m = 10
while m != 0:
    total += m
    while cont <=total:
        print('{}'.format(termo), end = ' - ')
        termo += r
        cont += 1
    print('PAUSA :0')
    m = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
input()