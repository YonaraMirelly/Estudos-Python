print('='* 20)
print('10 TERMOS DE UMA P.A')
print('='* 20)
pt = int(input('Primeiro termo: '))
r = int(input('Razão: ')) 
termo = pt
cont = 1
while cont <= 10:
    print('{} - '.format(termo), end='')
    termo += r
    cont +=1
print('FIM :0')
input()