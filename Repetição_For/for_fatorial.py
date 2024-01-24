n = int(input('Digite um número para calcular o seu fatorial: '))
f = 1
print('Calculando {}! = '.format(n), end='')
for i in range(n, 0 ,-1):
    print(i,end='')
    f = f * i
    print(' x ' if i >1 else ' = ', end='')
print('{}'.format(f))
input()