real = float(input('Quanto dihneiro você tem na sua carteira? R$ '))
dolar = real / 5.05
euro = real / 5.36
libra = real / 6.21
print('Com {:.2f}, você consegue comprar US {:.2f}, {:.2f} euros e {:.2f} em libras.'.format(real, dolar, euro, libra))
a = input()
