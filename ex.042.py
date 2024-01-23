#desafio dos três triângulos
print('\033[1;31m+\033[m'*20)
print('Analisador de Triângulos')
print('\033[33m=\033[m'*20)
a = float(input('\033[1mPrimeira reta do triângulo:\033[m '))
b = float(input('\033[1;31mSegunda reta do triângulo:\033[m '))
c = float(input('\033[1;34mTerceira reta do triângulo:\033[m '))
if a > b - c and b < a + c and c < a + b:
    print('\033[1;35mSIM! Ele pode ser um triângulo \033[m', end='')
    if a == b == c:
        print('\033[1;4;33mEQUILÁTERO.\033[m')
    elif a != b != c != a:
        print('\033[1;4;33mESCALENO.\033[m')
    else:
        print('\033[1;4;33mISÓSCELES.\033[m')
else:
    print('\033[1;36mNÃO... Ele não pode ser um triângulo:(\033[m')
input()