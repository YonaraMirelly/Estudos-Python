num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número \033[1;31m{}\033[m...'.format(num))
print('Unidade:\033[32m{}\033[m'.format(u))
print('Dezena:\033[32m{}\033[m'.format(d))
print('Centena:\033[32m{}\033[m'.format(c))
print('Milhar:\033[32m{}\033[m'.format(m))
input()