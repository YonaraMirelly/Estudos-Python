a = int(input('\033[1;33mPrimeiro valor:\033[m '))
b = int(input('\033[1;34mSegundo valor:\033[m '))
c = int(input('\033[1;32mTerceiro valor:\033[m '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('O MENOR valor digitado foi \033[1;35m{}\033[m'.format(menor))
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O MAIOR valor digitado foi \033[1;36m{}\033[m :)'.format(maior))
input()

