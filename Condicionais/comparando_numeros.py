#ler dois números
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
#comparação
if n1 > n2:
    print('O primeiro valor({}) é maior.'.format(n1))
elif n2 > n1:
    print('O segundo valor({}) é maior.'.format(n2))
else:
    print('NÃO existe valor maior, os dois são iguais.')
input()