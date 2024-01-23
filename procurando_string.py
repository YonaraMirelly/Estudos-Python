nome = str(input('Qual é seu nome completo? ' )).strip()
print('Há "Silva" no seu nome? \033[1;4;32;43m{}\033[m'.format('silva' in nome.lower()))
input()