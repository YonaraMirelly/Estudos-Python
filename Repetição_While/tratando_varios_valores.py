n = cont = soma = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma foi {}.'.format(cont, soma ))
input()