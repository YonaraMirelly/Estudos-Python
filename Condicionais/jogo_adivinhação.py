import random
computador = random.randint(0, 5) # o computador vai pensar em um numero entre 0 e 5
print('\033[35m-+-\033[m' *18)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('\033[36m-+-\033[m' *18)
jogador = int(input('Em qual número eu pensei? ')) # o jogador vai tentar adivinhar o número que o pc pensou :)
if jogador == computador:
    print('-' *25)
    print('\033[1;35;36mParabéns, você conseguiu adivinhar!\033[m')
    print('-' *25)
else:
    print('\033[1;35;36mQue pena, quem sabe numa próxima :)\033[m')
print('O número escolhido pelo computador foi \033[1;33m{}\033[m'.format(computador))
input()






