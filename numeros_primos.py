# é primo ou não?
n = int(input('Digite um número: \033[m'))
tot = 0
for c in range(1, n +1):
    if n % c == 0:
        print('\033[33m', end= ' ')
        tot += 1
    else:
        print('\033[31m', end= ' ')
    print('{}'.format(c), end= ' ')
print('\n\033[mO número {} foi dividido {} vezes.'.format(n, tot))
if tot == 2:
    print('E por isso ele é PRIMO :)')
else:
    print('E por isso ele NÃO é primo :(')
input()