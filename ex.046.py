# contagem regressiva com 1 segundo de pausa e depois vem a mensagem :)
from time import sleep
for c in range(10, -1, -1,):
    print(c)
    sleep(1)
print('\033[1;32m=-\033[m' * 30)
print('\033[1;33mFELIZ ANO NOVO!!!\033[m')
print('\033[1;34m=-\033[m' * 30)
input()


