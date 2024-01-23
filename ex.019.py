from random import choice
n1 = str(input('Nome do primeiro aluno(a): '))
n2 = str(input('Nome do segundo aluno(a): '))
n3 = str(input('Nome do terceiro aluno(a): '))
n4 = str(input('Nome do quarto aluno(a): '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno(a) escolhido foi \033[1;4;33;44m{}\033[m.'.format(escolhido))
input()
