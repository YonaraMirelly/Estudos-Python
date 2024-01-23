# ler os as notas
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
#condicionais aninhadas
if media >= 7:
    print('PARABÉNS!!! Você foi \033[1;32maprovado\033[m, com média {:.1f}.'.format(media))
elif media >=5 and media <= 7:
    print('RECUPERAÇÃO. Sua média foi {:.1f}, ou seja, você tem direito a \033[1;33mrecuperação\033[m.'.format(media))
elif media <=5:
    print('REPROVADO. Sua média foi {:.1f}, ou seja, infelizmente você foi \033[1;31mreprovado\033[m.'.format(media))
input()