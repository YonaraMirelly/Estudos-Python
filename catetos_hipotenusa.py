import math
b = float(input('Digite o valor do cateto oposto: '))
c = float(input('Digite o valor do cateto adjacente: '))
a = b**2 + c**2
print('A hipotenusa é igual a \033[7;37m{:.2f}\033[m.'.format(math.sqrt(a)))
input()
