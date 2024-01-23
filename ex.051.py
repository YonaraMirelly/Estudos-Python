print('=' * 20)
print('10 TERMOS DE UMA P.A.')
print('=' * 20)
pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = pt + (10-1) * r
for c in range(pt, decimo + r, r):
    print('{}'.format(c), end=' - ')
print('FIM :)')
input()