n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
cores = {'limpa': '\033[m', 'verde': '\033[1;32m', 'amarelo': '\033[1;33m', 'azul': '\033[1;34m'}
print('A soma entre {}{}{} e {}{}{} é igual a {}{}{}.'.format(cores['verde'],n1,cores['limpa'],cores['amarelo'],n2,cores['limpa'],cores['azul'],s,cores['limpa']))
a = input()