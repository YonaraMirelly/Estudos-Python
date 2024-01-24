import random
computador  = random.randint(0,10)
pc = computador
tenta = 0
print('O computador pensou em um número entre 0 e 10. Será que você consegue adivinhar qual foi? ')
print('Em que número o pc pensou? ')
acertou = False
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    tenta +=1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente de novo.')
        elif jogador > computador:
            print('Menos... tente de novo.')
print('Acertou! Com um total de {} tentativas, \033[1;32mParabéns!\033[m'.format(tenta))
print('O pc pensou no número {} :)'.format(pc))
input()