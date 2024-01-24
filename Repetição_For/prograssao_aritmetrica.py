print('=' * 20)
print('\033[1m10 TERMOS DE UMA P.A.\033[m')
print('=' * 20)
pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = pt + (10-1) * r
for c in range(pt, decimo + r, r):
    print('{}'.format(c), end=' - ')
print('FIM :)')
input()