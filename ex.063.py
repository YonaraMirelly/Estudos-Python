#sequência de fibonacci
print('-' * 25)
print('SEQUÊNCIA DE FIBONACCI')
print('-' * 25)
n = int(input('Quantos Termos Você Quer Mostrar? '))
t1 = 0
t2 = 1
print('{} - {} -'.format(t1,t2), end = '')
cont = 3
while cont <=n:
    t3 = t1+t2
    cont +=1
    print(' {} -'.format(t3), end= '')
    t1 = t2
    t2 = t3
print('FIM')
input()
