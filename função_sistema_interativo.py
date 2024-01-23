from time import sleep
c = ('\033[m', #0 - sem cor
     '\033[0;31m', #1 - vermelho
     '\033[0;32m', #2 - verde
     '\033[0;33m', #3 - amarelo
     '\033[0;34m', #4 - azul
     '\033[0;35m', #5 - roxo
     '\033[0;36m', #6 - ciano
     '\033[0;37m', #7 - cinza
     )
def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 6)
    help(com)
    sleep(1)
def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c[0], end='')
    sleep(1)

#programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA pyHELP', 5)
    comando = str(input('Função ou biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 3)
input()