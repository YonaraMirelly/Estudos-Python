from datetime import date
ano = int(input('Que ano quer analisar? Digite 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    print('O ano de {} \033[1;4;35mÉ BISSEXTO.\033[m'.format(ano))
else:
    print('O ano de {} \033[1;4;31mNÃO\033[m \033[1;4;35mÉ BISSEXTO\033[m.'.format(ano))
input()