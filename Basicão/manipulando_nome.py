nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando o seu nome...')
nomea = nome.upper()
nomeb = nome.lower()
print('Seu nome em maiúsculo é \033[1;35;47m{}\033[m'.format(nomea))
print('Seu nome em minúsculo é \033[1;35;47m{}\033[m'.format(nomeb))
print('Seu nome tem ao todo \033[1;35m{}\033[m letras'.format(len(nome)-nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é \033[1;45m{}\033[m e ele tem \033[1;35m{}\033[m letras'.format(separa[0], len(separa[0])))
input()


