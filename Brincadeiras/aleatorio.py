# def topo(peso=0):
#     print('-' * 20)
#     print(f'o maior peso até agora é {peso}')
#     print('-' * 20)
# def rodada():
#     peso = 0
#     nome_pesado = ''
#     topo(peso)
#     for i in range(0,3):
#         nome = input('nome da pessoa: ')
#         p = float(input(f'Peso de {nome}: '))
#         if p > peso:
#             peso = p
#             nome_pesado = nome
#         topo(peso)
#     topo(peso)
#     print(f'A pessoa mais pesada foi {nome_pesado} com {peso}kg.')
# rodada()

# def soma(a,b):
#     print(f'recebi {a}')
#     print(f'recebi {b}')
#     print(f'somando {a} + {b} = {a + b}')
# soma(5,5)

# def par_impar(a):
#     if a % 2 == 0:
#         return 'par'
#     else:
#         return 'impar'
# print(par_impar(4))

# def soma(a, b):
#     a +=1
#     b +=2
#     print(f'a soma vale {a+b}')
#     return a, b
# x = 4
# y = 8
# x, y = soma(x, y)
# print(x,y)

def fib(n):
    a, b = 0, 1
    lista = []
    for i in range(1, n+1):
        lista += [a]
        a, b = b, a + b

    return lista

print(fib(13))