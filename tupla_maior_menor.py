from random import randint
pc = (randint(0,10),randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print('Os valores sorteados foram: ', end = '')
for numeros in pc:
    print(f'{numeros}', end = ' ')
print(f'\nO MAIOR valor sorteado é {max(pc)}.')
print(f'O MENOR valor sorteado é {min(pc)}.')