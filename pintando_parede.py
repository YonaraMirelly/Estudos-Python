compri = float(input('Digite o comprimento da parede: '))
largu = float(input('Digite a largura da parede: '))
area = (compri * largu)
x = area / 2
print('Sua parede tem a dimensão de \033[31m{}\033[m x \033[32m{}\033[m e sua área é de \033[33m{:.2f}\033[m'.format(compri, largu, area))
print('Para pintar essa parede, você precisará de \033[35m{:.2f}\033[m litros de tinta'.format(x))
input()