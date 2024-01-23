# ler o ano de nascimento de 7 pessoas e dizer quem é de maior e quem é de menor.
from datetime import date
anoatual = date.today().year
totalmaior = 0
totalmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = anoatual - nasc
    if idade >= 18:
        totalmaior += 1
    else:
        totalmenor += 1
print('Ao todo, tivemos {} pessoas \033[1mmaiores de idade.\033[m'.format(totalmaior))
print('E também tivemos {} pessoas \033[1mmenores de idade\033[m'.format(totalmenor))
input()