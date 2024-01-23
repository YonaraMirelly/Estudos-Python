dia = float(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
c1 = dia *60
c2 = km *0.15
c3 = c1 + c2
print('O total a pagar é de \033[1;32mR$\033[m\033[1;35m{}\033[m.'.format(c3))
input()
