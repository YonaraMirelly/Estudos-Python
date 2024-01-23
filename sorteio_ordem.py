from random import shuffle
n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('quarto nome: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será:\n\033[1;4;32;41m{}\033[m.'.format(lista))
input()