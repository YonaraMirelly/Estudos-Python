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

#n = int(input('Fatorial de -> '))
#f = 1
#c = n
#if n >20:
#    print('Digite um número menor doq 20!!!!!!!')
#else:
#    while c >0:
#        print(f'{c}', end = '')
#        print(' x ' if c>1 else ' = ', end = '')
#        f *=c
#        c-=1
#    print(f'{f}')
#print('fim do programa!')

#def Fatorial(n):
#    f = 1
#    c = n
#    if n >20:
#        print('Digite um número menor doq 20')
#    else:
#        while c>0:
#            print(f'{c}', end = '')
#            print(f' x ' if c>1 else ' = ', end = '')
#            f *=c
#            c-=1
#        print(f'{f}')
#    print('fim do programa')
#Fatorial(2)


#contador = 0
#numero = 2
#while contador <15:
#    divisor = 2
#    while divisor < numero:
#        if numero % divisor == 0:
#            break
#        divisor +=1
#    else:
#        print(numero, end = ' - ')
#        contador +=1
#    numero +=1

#def primo(n):
#    contador = 0
#    numero = 2
#    while contador <n:
#        divisor = 2
#        while divisor < numero:
#            if numero %divisor ==0:
#                break
#            divisor+=1
#        else:
#            print(numero, end = ' - ')
#            contador +=1
#        numero +=1
#primo(20)

#base = int(input("base -> "))
#exp = int(input('Expoente -> '))
#resultado = 1
#cont = 0
#while cont<exp:
#    resultado *=base
#    cont +=1
#print(f'{resultado}')

#def Potencia(base, exp):
#    cont = 0
#    result = 1
#    while cont<exp:
#        result *=base
#        cont +=1
#    print(f'{result}')
#Potencia(2,3)

#cont = 0
#while cont < 5:
#    valor = int(input("Digite um número -> "))
#    if valor<0:
#        print('Não pode numero negativo mô')
#        break
#    cont+=1
#else:
#    print('Os 5 dados foram inseridos com sucesso!')
#print('fim do programa!')

#def Valores(n = 5):
#    cont = 0
#    while cont<n:
#        numero = int(input('Número -> '))
#        if numero <0:
#            print('não pode negativo')
#            break
#        cont +=1
#    else:
#        print('Os 5 valores adicionados com sucesso!')
#Valores()

#while True:
#    n = int(input('Tabuada de -> '))
#    print(f'TABUADA DE {n}:')
#    contador = 0
#    while contador <= 10:
#        print(f'{n} x {contador} = {n * contador}')
#        contador +=1
#    continuar = str(input("Deseja ver a tabuada de outro número? [S/N] ")).lower()
#    if continuar != "S":
#        print('fim')
#        break

#def Tabuada(numero):
#    while True:
#        cont = 0
#        while cont <=10:
#            print(f'{numero} x {cont} = {numero * cont}')
#            cont +=1
#        continuar = input('Deseja continuar? [S/N] ').lower()
#        if continuar != 'S':
#            print('fim')
#            break
#Tabuada(4)





