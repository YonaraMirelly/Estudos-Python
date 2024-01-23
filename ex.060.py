#ler qualquer número
num = int(input('Digite um número para calcular o seu Fatorial: '))
c = num
f = 1
print('Calculando {}! = '.format(num), end='')
#mostrar o fatorial de num
while c > 0:
    print('{}'.format(c), end= '')
    f = f * c
    c -=1
    print(' x ' if c> 0 else ' = ', end='')
print('{}'.format(f))
input()
