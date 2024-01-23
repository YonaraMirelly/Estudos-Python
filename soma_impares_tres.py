#tem que ser de 1 a 500
soma = 0
cont = 0
for n in range(1, 501, 2 ):
    if n %3 ==0:
        cont = cont + 1
        soma = soma + n
print('A soma de todos os {} valores solicitados, é igual a {}.'.format(cont, soma))
input()