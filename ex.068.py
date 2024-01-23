from random import randint
print('-='*30)
print('\033[1;36mVAMOS JOGAR PAR OU ÍMPAR\033[m')
print('-='*30)
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    t = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total:{t}', end=' ')
    print('DEU PAR'if t % 2== 0 else 'Deu Ímpar')
    if tipo == 'P':
        if t % 2==0:
            print('\033[1;32mVOCÊ VENCEU!\033[m')
            v +=1
        else:
            print('\033[1;31mVOCÊ PERDEU!\033[m')
            break
    elif tipo == 'I':
        if t % 2 == 0:
            print('\033[1;31mVOCÊ PERDEU!\033[m')
            break
        else:
            print('\033[1;32mVOCÊ VENCEU!\033[m')
            v +=1
        print('Vamos jogar novamente...')
print(f'GAME OVER! Você Terminou com {v} vitórias!')
input()