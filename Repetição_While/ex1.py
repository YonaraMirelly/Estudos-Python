#n = int(input("Digite um valor-> "))
#a, b = 0, 1
#while a<=n:
#    print(a, end = ' - ')
#    a, b = b, a + b
#print('fim')

#x = 10
#while x >=0:
#    x-=1
#    if x%2 != 0:
#        continue
#    print(f'{x} é par')
#else:
#    print('fim')

#def Fibonacci(n):
#    a, b = 0, 1
#    while a <=n:
#        print(a, end = ' - ')
#        a, b = b, a+b
#    print('fim')
#Fibonacci(13)

#def Par(x):
#    while x >=0:
#        x-=1
#        if x%2 !=0:
#            continue
#        print(f'{x} é par')
#    else:
#        print('fim')
#Par(20)

#cont = 0
#sair = 1
#while sair != 0:
#    idade = int(input('idade: '))
#    altura = float(input('altura: '))
#    sair = int(input('Sair? [0] '))
#    print('-'*30)
#    if (idade>13) and (altura<1.5):
#        cont +=1
#print(f'{cont} pessoas tem idade maior que 13 e possuem altura inferior a 1.5m')

#def Maior13():
#    cont = 0
#    sair = 1
#    while sair !=0:
#        idade = int(input('idade: '))
#        altura = float(input('altura: '))
#        sair = int(input('sair? '))
#        print('-'*30)
#        if (idade>13) and (altura<1.5):
#            cont +=1
#    print(f'{cont} pessoas tem idade maior que 13 e possuem altura inferior a 1.5m')
#Maior13()

#l = []
#while True:
#    n = int(input('número-> '))
#    sair = int(input('sair [99] '))
#    if sair == 99:
#        break
#    elif n %2 == 0 or n<0:
#        continue
#    l.append(n)
#print(f'{l} é ímpar positivo.')

#def Impar():
#    l = []
#    while True:
#        n = int(input('núemro-> '))
#        sair = int(input('sair? [99] '))
#        if sair == 99:
#            break
#        elif n%2 == 0 or n<0:
#            continue
 #       l.append(n)
#    print(f'{l} são numeros impares positivos.')
#Impar()

n = int(input('Fatorial de -> '))
c = n
f = 1
while c>0:
    print(f'{c}', end = '')
    print(' x ' if c >1 else ' = ', end = '')
    f *=c
    c-=1
print(f'{f}')

