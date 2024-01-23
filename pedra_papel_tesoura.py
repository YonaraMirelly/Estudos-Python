#jogo do pedra, papel e tesoura :0
from random import randint
itens = ('Pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('Suas opções:')
print('[0] PEDRA')
print('[1] PAPEL')
print('[2] TESOURA')
jogador = int(input('Qual é a sua jogada? '))
print('-=' * 11)
print('\033[1;4;35mComputador\033[m jogou {}.'.format(itens[computador]))
print('\033[1;4;36mJogador\033[m jogou {}'.format(itens[jogador]))
print('-=' * 11)
#condicionais aninhadas
if computador == 0: #pedra
    if jogador == 0:
        print('\033[1;35mEMPATE\033[m')
    elif jogador == 1:
        print('\033[1;32mJOGADOR VENCEU\033[m')
    elif jogador == 2:
        print('\033[1;31mJOGADOR PERDEU\033[m')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1: #papel
    if jogador == 0:
        print('\033[1;31mJOGADOR PERDEU\033[m')
    elif jogador == 1:
        print('\033[1;35mEMPATE\033[m')
    elif jogador == 2:
        print('\033[1;32mJOGADOR VENCEU\033[m')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2: #tesoura
    if jogador == 0:
        print('\033[1;31mJOGADOR PERDEU\033[m')
    elif jogador == 1:
        print('\033[1;32mJOGADOR VENCEU\033[m')
    elif jogador == 2:
        print('\033[1;35mEMPATE\033[m')
    else:
        print('JOGADA INVÁLIDA')
input()

