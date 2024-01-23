# o cara vai dizer um número e vai escolher uma das opções
num =  int(input('Digite um número inteiro: '))
print('''Escolha uma das opções:
[1] Converter para Binário
[2] Converter para Octal
[3] Converter para Hexadecimal''')
opçao = int(input('Sua escolha: '))
#condicionais aninhadas
if opçao == 1:
    print('O número {} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opçao == 2:
    print('O número {} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opçao == 3:
    print('O número {} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('opção inválida. Tente novamente.')
input()
