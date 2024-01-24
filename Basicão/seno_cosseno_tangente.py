from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
coss = cos(radians(angulo))
tang = tan(radians(angulo))
print(f'O ângulo de \033[1;32m{angulo:.1f}\033[m tem o SENO de \033[1;35m{seno:.2f}\033[m.')
print(f'O COSSENO de \033[1;35m{coss:.2f}\033[m.') 
print(f'E a TANGENTE de \033[1;35m{tang:.2f}\033[m.')
input()
