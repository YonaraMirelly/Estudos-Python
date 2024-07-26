import time


def maioridade(idade):
    if idade >= 21:
        return 'vc eh tem mais de 21 anos.'
    else:
        return 'vc ainda eh menor de idade, ou seja, menos de 21 anos.'

def idade(ano_atual, nasceu):
    idade = int(ano_atual - nasceu)
    return idade

# ano_atual = int(input('ano atual - '))
# nasceu = int(input('ano de nascimento - '))
# i = idade(ano_atual, nasceu)
# print(maioridade(i))
def par_impar(n):
    if n%2 == 0:
        return 'par'
    else:
        return 'impar'

# n = int(input('numero - '))
# print(par_impar(n))

def imc(massa, altura):
    imc = massa//(altura**2)
    if 18.5 > imc < 25:
        return 'peso ideal'
    elif imc < 18.5:
        return 'magro'
    else:
        return 'gordo'
    
# massa = float(input('massa - '))
# altura = float(input('altura - '))
# print(imc(massa, altura))

def apto(idade):
    if idade >= 18:
        print('--------------')
        print(f'idade = {idade}')
        print('vc está apto a dirigir')
        print('--------------')
        return ''
    else:
        print('--------------')
        print(f'idade = {idade} ')
        print('vc não está apto a dirigir')
        print('--------------')
        return ''

# ano_atual = int(input('ano atual - '))
# nasceu = int(input('ano de nascimento - '))
# i = idade(ano_atual, nasceu)
# print(apto(i))

def titulo(nome):
    print('-'*20)
    print(f'{nome}'.center(17))
    print('-'*20)
    return ''

def passei(n1, n2):
    media = (n1+n2)/2
    if media >= 7:
        print('-'*20)
        print(f'Média: {media}')
        print('vc passou')
        print('-'*20)
        return ''
    elif media <7:
        print('-'*20)
        print(f'Média: {media}')
        print('vc não passou')
        print('-'*20)
        return ''

# n = input('Digite o título - ')
# print(titulo(n))
# n1 = float(input('Digite a nota 1 - '))
# n2 = float(input('Digite a nota 2 - '))
# print(passei(n1, n2))

# c = 0
# while c <=10:
#     print(c)
#     c += 1
# print('eh sobre isso')

# soma = 0
# c = 1
# maior = None
# menor = None
# while c <= 10:
#     n = int(input(f'{c} número - '))
    
#     if maior is None or n > maior:
#         maior = n
#     if menor is None or n < menor:
#         menor = n
    
#     soma += n
#     c+=1
# print(soma)
# print(maior)
# print(f'menor - {menor}')

# def fat(n):
#     if n <= 1:
#         return n
#     else:
#         return n * fat(n-1)

# print(fat(8))

# def tab(n):
#     c = 0
#     while c<=10:
#         print(f'{n} x {c} = {n*c}')
#         c+=1
#     return ''
# print(tab(int(input('quer ver qual número? '))))


# c = 1
# neg = 0
# valores = []
# while c<=5:
#     n = int(input('numero - '))
#     if n < 0:
#         neg+=1
#         valores += [n]
#     c+=1
# print(neg)
# print(valores)

# n = int(input('digite um numero - '))
# c = n
# f = 1
# while True:
#     print(c, end = ' - ')
#     f *= c
#     c -= 1
#     if c == 0:
#         break
# print(f'o fatorial é {f}')

# n = int(input('digite um numero - '))
# c = 1
# contdiv = 0
# while c <= n:
#     print(c, end = ' - ')
#     if n % c == 0:
#         contdiv +=1

#     c+=1
# if contdiv == 2:
#     print('o número é primo! ')
# else:
#     print('o número não é primo! ') 

# n = int(input())
# tot = soma = 0

# for i in range(1, 6+1):
#     n = int(input('digite um valor - '))
#     if n >= 0 and n <=10:
#         tot += 1
#         if n % 2 != 0:
#             soma +=n

# print(f'ao todo foraam {tot} valores entre 0 e 10.')
# print(f'somando os valores impares foi {soma}')


# import time
# inicio = time.time()
# for c1 in range(1, 3+1):
#     for c2 in range(1, 3+1):
#         print(c1, c2)

# fim = time.time()
# print(f'durou {fim-inicio} seg')


def sequencia(n):
    lista = []
    a, b = 0, 1
    while len(lista) <= n:
        lista += [a]
        a, b = b, a+b
    return lista
print(sequencia(5))