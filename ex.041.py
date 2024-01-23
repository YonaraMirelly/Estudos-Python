#título bonitinho
from datetime import date
print('\033[1;36m+\033[m' * 30)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('\033[1;36m+\033[m' * 30)
#ler ano de nascimento
num = int(input('Informe o ANO em que você nasceu: '))
anoatual = date.today().year
ano = anoatual - num
print('Você tem {} anos de idade.'.format(ano))
#condições aninhadas (categorias)
if ano <= 9:
    print('Você se encaixa na categoria \033[1;4mMIRIM.\033[m')
elif ano > 9 and ano <=14:
    print('Você se encaixa na categoria \033[1;4mINFANTIL.\033[m')
elif ano > 14 and ano <=19:
    print('Você se encaixa na categoria \033[1;4mJÚNIOR.\033[m')
elif ano > 19 and ano <= 25:
    print('Você se encaixa na categoria \033[1;4mSÊNIOR.\033[m')
elif ano > 25:
    print('VocÊ se encaixa na categoria \033[1;4mMASTER.\033[m')
input()

