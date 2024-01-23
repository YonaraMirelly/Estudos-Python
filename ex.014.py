celsius = float(input('Informe a temperatura em graus celsius: '))
f = (celsius * 9)/5
f1 = f + 32
print('A temperatura de \033[1;33m{}\033[m°C corresponde a \033[1;36m{}\033[mF.'.format(celsius, f1))
input()