nome = str(input('Digite o seu nome completo: ')).strip()
p = nome.split()
print('Seu primeiro nome é \033[4;33;41m{}\033[m'.format(p[0]))
print('Seu último nome é \033[4;33;41m{}\033[m'.format(p[len(p)-1]))
input()