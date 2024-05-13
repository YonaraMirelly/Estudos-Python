string = str(input())
vogais = ['a', 'e', 'i', 'o', 'u']
risada = ''.join(x for x in string if x in vogais)


if risada == risada[::-1]:
    print('S')
else:
    print('N')
