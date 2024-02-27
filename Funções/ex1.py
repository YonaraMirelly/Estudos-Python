#def multi(a,b,c):
#    return a*b*c
#print(multi(1,2,3))

#def Fatorial(num):
#    c = num
#    f = 1
#    while c>0:
#        print(f'{c}', end = '')
#        print(' x ' if c>1 else ' = ', end = '')
#        f*=c
#        c-=1
#    print(f'{f}')
#Fatorial(5)

#def fibonacci(n):
#    a = 0
#    b = 1
#    while a<=n:
#        print(a, end = ' - ')
#        a,b = b, a+b
#fibonacci(5)


#def Concatena(*args):
#    tamanho = len(args)
#    conca = ''.join(map(str,args))
#    return tamanho, conca
#print(Concatena(1,2,'yonara', 'mirelly'))
    

#def Remover(lista):
#    palavras_filtradas = [palavra for palavra in lista if not palavra.lower().startswith('a')]
#    return palavras_filtradas   
#lista = ['maçâ', 'amanhâ', 'Amanda']
#print(Remover(lista))

#def Quadrado(intervalo):
#    quadrado = [x**2 for x in range(intervalo) if x %2==0]    
#    return quadrado
#print(Quadrado(11))

#def Digito(numero):
#    s = str(numero)
#    a = len(s)
#   return a
#print(Digito(12349))

#def Retorna(numero):
#    if numero >0:
#        return 'P'
#    else:
#        return "N"
#print(Retorna(-2))

#def Inverso(numero):
#    s = str(numero)
#    inverso = s[::-1]
#    return inverso
#print(Inverso(123))

