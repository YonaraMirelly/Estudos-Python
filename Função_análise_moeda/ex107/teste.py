import moeda

p = float(input('digite o preço R$'))
print(f'A metade de {p} é R${moeda.metade(p)}')
print(f'O dobro de {p} é R${moeda.dobro(p)}')
print(f'Aumentando 10% temos R${moeda.aumentar(p, 10)}')
print(f'Diminuindo em 30% temos R${moeda.diminuir(p, 30)}')


