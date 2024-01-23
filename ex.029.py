velocidade = float(input('Qual é a velocidade atual do seu carro? '))
multa = (velocidade-80) *7
if velocidade < 80:
    print('\033[1;32;47mTenha um bom dia! Dirija com segurança :)\033[m')
else:
    print('\033[1;31;47mMULTADO! Você excedeu o limite de 80km/h\033[m')
    print('Você deve pagar uma multa de \033[32mR${:.2f}\033[m'.format(multa))
input()
