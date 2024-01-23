num = int(input('Me diga um número qualquer: '))
resultado = num % 2
if resultado == 0:
    print('Seu número é \033[1;4;36mpar\033[m')
else:
    print('Seu número é \033[1;4;34mímpar\033[m')
input()