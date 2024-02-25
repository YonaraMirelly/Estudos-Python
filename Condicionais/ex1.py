#n = int(input("Número: "))
#if n%2 ==0:
#    print(f'{n} é par')
#else:
#    print(f'{n} é ímpar')

#def ParImpar(numero):
#    if numero %2 ==0:
#        print(f'{numero} é par')
#    else:
#        print(f'{numero} é ímpar')
#ParImpar(9)

#t = float(input("Temperatura-> "))
#if t  >= 39:
#    print('Febre Alta')
#elif 39 > t >= 37:
#    print('Febril')
#elif t <=37:
#    print('Sem febre!')

#def analisa(t):
#    if t >=39:
#        print('Febre Alta')
#    elif 39 > t >=37:
#        print('Febril')
#    elif t < 37:
#        print('Sem febre!')
#analisa(38)

#d = float(input('km-> '))
#t = int(input('horas-> '))
#media = d/t
#if media >110:
#    print(f'{media} ultrapassou o limite!')
#else:
#    print(f'{media} está bem :)')

#def velocidade(distancia, hora):
#    media = distancia / hora
#    if media > 110:
#        print(f'{media} ultrapassou o limite!')
#    else:
#        print(f'{media} está dentro do limite!')
#velocidade(500, 2)

#ano = int(input("ano-> "))
#if (ano %4 == 0 and ano %100 !=0) or (ano%400 == 0):
#    print(f'{ano} é bissexto')
#else:
#    print(f'{ano} NÃO é bissexto')

#def bissexto(valor):
#    if (valor%4 == 0 and valor%100!=0) or (valor%400 ==0):
#        print('ano bisssexto')
#    else:
#        print('não é bissexto')
#bissexto(2023)

#a = int(input('número1 -> '))
#b = int(input('número2 -> '))
#c = int(input('número3 -> '))

#if (a>b and a>c) and (b>c):
#    maior = a
#    meio = b
#    menor = c
#elif (b>a and b>c) and (a>c):
#    maior = b
#    meio = a
#    menor = c
#elif (c>a and c>b) and (a>b):
#    maior = c
#    meio = a
#    menor = b
#else:
#    maior = c
#    meio = b
#    menor = a
#print(maior, meio, menor)

#def Decrescente(a,b,c):
#   if (a>=b and a>=c):
#        maior = a
#        if b>=c:
#            meio = b
#            menor = c
#        elif c>=b:
#            meio = c
#            menor = b
#    elif (b>=a and b>=c):
#        maior = b
#        if a>=c:
#            meio = a
#            menor = c
#        elif c>=a:
#            meio = c
#            menor = a
#    elif (c>=a and c>=b):
#        maior = c
#        if a>=b:
#            meio = a
#            menor = b
#        elif b>=a:
#            meio = b
#            menor = a
#    return maior, meio, menor
#print(Decrescente(100,100,4000))

#a = float(input("Produto1: "))
#b = float(input('Produto2: '))
#c = float(input("Produto2: "))
#if a<b and a<c:
#    print(f'{a} é o mais barato.')
#elif b<a and b<c:
#    print(f'{b} é o mais barato.')
#elif c<a and c<b:
#    print(f'{c} é o mais barato.')
#else:
#    print('não existe apenas um único produto barato!')

#def MaisBarato(a,b,c):
#    if a<b and a<c:
#        print(f'{a} é o mais barato.')
#    elif b<a and b<c:
#        print(f'{b} é o mais barato.')
#    elif c<a and c<b:
#        print(f'{c} é o mais barato.')
#    else:
#        print('Não existe apenas um único número que seja o mais barato!')    
#MaisBarato(351,500,350)


