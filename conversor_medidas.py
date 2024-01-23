metros = int(input("Digite seu valor em metros: "))
cent = metros * 100
mili = metros * 1000
print('Seu valor vale \033[31m{}\033[m em centímetros e \033[33m{}\033[m em milímetros.'.format(cent, mili))
a = input()