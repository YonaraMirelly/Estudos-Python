# ler a idade p alistamento militar
from datetime import date
data = int(input('Informe o ANO de nascimento: '))
# fazer os cálculos pra descobrir o ano da pessoa
anoatual = date.today().year
ano = anoatual - data
print('Quem nasceu em {} tem {} anos em {}.'.format(data, ano, anoatual))
#condicionais aninhadas
if ano == 18:
    print('Está na hora de se alistar!!!')
elif ano < 18:
    print('Faltam {} anos para você se alistar.'.format(18 - ano))
    print('Seu alistamento será em {}.'.format(anoatual + (18 - ano)))
elif ano > 18:
    print('Você passou do tempo de se alistar em {} anos.'.format(ano - 18))
    print('Você deveria ter se alistado em {}.'.format(anoatual - (ano - 18)))
input()

