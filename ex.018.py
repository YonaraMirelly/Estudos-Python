from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
coss = cos(radians(angulo))
tang = tan(radians(angulo))
print('O ângulo de \033[1;32m{:.1f}\033[m tem o SENO de \033[1;35m{:.2f}\033[m.\n O COSSENO de \033[1;35m{:.2f}\033[m.\n E a TANGENTE de \033[1;35m{:.2f}\033[m.'.format(angulo, seno, coss, tang))
input()
