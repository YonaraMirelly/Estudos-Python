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

#def Imposto (taxa, custo):
#    imposto = custo *(taxa/100)
#    alterado = custo + imposto
#    print(f'O custo final, incluindo o imposto é de {alterado}')
#Imposto(10, 100)

#def MDC(a,b):
#    if b == 0:
#        return a
#    else:
#        return MDC(b, a%b)
#resultado = MDC(15,18)
#print(f'O mdc é {resultado}')

#def interface(nomes):
#    return nomes
#def bd(lista, arq):
#    with open(arq, 'w') as file:
#        file.write('\n'.join(lista))
#def main():
#    lista_nomes = []
#    while True:
#        nome = str(input('Nome -> '))
#        lista_nomes.append(nome)
#        op = input('quer continuar? ').upper()
#        if op == "N":
#            print('Nomes salvos com sucesso!')
#            break
#    bd(lista_nomes, 'nomes.txt')
#main()

#def main():
#    lista_pessoas = ['Ana', 'Arthur', 'Alice', 'Amanda']
#    maior_nome = Analisar(lista_pessoas)
#    Imprimir(maior_nome)

#def arquivo(lista, arq):
#    with open(arq, 'w') as file:
#        file.write('\n'.join(lista))

#def Analisar(lista):
#    lista_a = [nome for nome in lista if nome.lower().startswith('a')]
#    maior_nome = ''
#    for nome in lista_a:
#        if len(nome) > len(maior_nome):
#            maior_nome = nome
#    arquivo(lista_a, 'nome_A.txt')
#    return maior_nome

#def Imprimir(nome):
#    print(f'O maior nome que começa com "A" é {nome}')

#main()

#def Converter(n1, n2):
#    if n1<12:
#        novo = n1 + 12
#        hora = 'PM'
#        return f'{novo}:{n2} {hora}'
#    elif n1 == 12:
#        novo = n1-12
#        hora = 'AM'
#        return f'{novo}:{n2} {hora}'
#    elif n1 == 00:
#        novo = n1+12
#        hora = 'PM'
#        return f'{novo}:{n2} {hora}'
#    elif n1>12:
#        novo = n1-12
#        hora = 'AM'
#        return f'{novo}:{n2} {hora}'   
#print(Converter(13, 30))

#def main():
#    nome = input('nome: ').lower()
#    print(T(nome))
#def T(nome):
#    tras = nome[::-1].upper()
#    return tras
#main()

#def Intro():
#    data = input('Digite sua data de nascimento [dd/mm/aaaa]-> ')
#    return print(Converte(data))

#def Converte(data):
#    data_split = data.split('/')
#    dia = data_split[0]
#    mes = int(data_split[1])
#    ano = data_split[2]
#    meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

#    nome_mes = meses[mes-1]

#    return f'Você nasceu em {dia} de {nome_mes} de {ano}'

#Intro()

