#ler peso e altura
p = float(input('Digite o seu peso em kg: '))
a = float(input('Digite a sua altura em metros: '))
#calculo imc
imc = p / (a ** 2)
print('Seu IMC é de {:.1f}.'.format(imc))
#condições aninhadas
if imc <= 18.5:
    print('Você está \033[1;4mABAIXO DO PESO.\033[m')
elif imc > 18.5 and imc <= 25:
    print('Você está no \033[1;4mPESO IDEAL.\033[m')
elif imc > 25 and imc <= 30:
    print('Você está no \033[1;4mSOBREPESO.\033[m')
elif imc > 30 and imc <=40:
    print('Você está na \033[1;4mOBESIDADE.\033[m')
else:
    print('\033[1;31mATENÇÃO: OBESIDADE MÓRBIDA!\033[m')
input()