num = int(input('Digite um número para ver sua tabuada: '))
for n in range(1, 11):
    print('{} x {} = {}'.format(num, n, num*n))
input()