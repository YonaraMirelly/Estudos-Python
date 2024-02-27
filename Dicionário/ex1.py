
#pessoas = {}
#nome = input('nome - ')
#idade = int(input('idade - '))
#end = input('end - ')
#tel = int(input('tel - '))
#pessoas['nome'] = nome
#pessoas['idade'] = idade
#pessoas['end'] = end
#pessoas['tel'] = tel
#for v, elemento in pessoas.items():
#    print(f'{v} - {elemento}')


#qtde = int(input('quantas pessoas? '))
#pessoas = {}
#pessoas_dic = {}
#for i in range(qtde):
#    nome = input('nome - ')
#    idade = input('idade - ')
#    tel = input('telefone - ')
#    cpf = input('CPF - ')
#    pessoas[cpf] = [nome, idade, tel]
#    pessoas_dic[cpf] = {'nome': nome, 'idade': idade, 'telefone': tel, 'cpf': cpf}
#while True:
#    busca = str(input('vc quer os dados de quem? '))
#    if busca in pessoas_dic:
#        print(f'{pessoas[busca]}')
#    else:
#        print('pessoas não encontrada!')
#    rep = input('quer de mais alguém? ').upper()
#    if rep == "N":
#        break
#print('fim')

#d = {}
#d2 = {}

#while True:
#    nome = input('nome - ')
#    idade = int(input('idade - '))
#    cpf = input('cpf - ')
#    d[cpf] = {'nome': nome, 'idade': idade, 'cpf': cpf}
#    rep = input('deseja continuar? ').upper()
#    if rep == "N":
#        for elemento in d:
#            if d[cpf]['idade'] <18:
#                d1 = d.copy()
#                d2 = d1.pop(cpf)
#               print(f'Lista completa -> {d}')
#               print(f'Lista de menores -> {d2}')
    
#principal = {}
#backup = {}
#def Imprimir():
#    for chave, valor in principal.items():
#        print(f'{chave} - {valor}')
#    principal.clear()
#while True:
#    chave = input('chave: ')
#    valor = input('valor: ')
#    principal[chave] = valor
#    backup[chave] = valor
#    if len(principal) == 5:
#        Imprimir()

#matriz = {}
#par = impar = 0
#linha = int(input('linhas - '))
#coluna = int(input('coluna - '))

#for i in range(linha):
#    for j in range(coluna):
#        elemento = int(input(f'{i,j} -> '))
#        matriz[(i, j)] = elemento

#for i in range(linha):
#    for j in range(coluna):
#        print(f'[{matriz[(i,j)]}]', end = '')
#    print()

#for elemento in matriz.values():
#    if elemento %2 == 0:
#        par += elemento
#    else:
#        impar +=elemento

#print(f'soma par = {par}')
#print(f'soma impar = {impar}')

#from random import randint
#m1 = {}
#m2 = {}
#linha1 = int(input('linha1 - '))
#coluna1 = int(input('coluna1 - '))
#linha2 = coluna1
#coluna2 = int(input('coluna2 - '))
#for i in range(linha1):
#    for j in range(coluna1):
#        m1[(i,j)] = randint(0,1)
#print('matriz 1')
#for i in range(linha1):
#    for j in range(coluna1):
#        print(f'[{m1[(i,j)]:^5}]', end = '')
#    print()
#for i in range(linha2):
#    for j in range(coluna2):
#        m2[(i,j)] = randint(0,1)
#print('matriz 2')
#for i in range(linha2):
#    for j in range(coluna2):
#        print(f'[{m2[(i,j)]:^5}]', end = '')
#    print()
#print('multiplicação')
#multi = {}
#for i in range(linha1):
#    for j in range(coluna2):
#        multi[(i,j)] = 0
#        for k in range(linha2):
#            multi[(i,j)] += m1[(i,k)] * m2[(k,j)]
#for i in range(linha1):
#    for j in range(linha2):
#        print(f'[{multi[(i,j)]:^5}]', end = '')
#    print()
#from random import randint
#d = {}
#dimensao = int(input('dimensão - '))
#for i in range(dimensao):
#    for j in range(dimensao):
#        d[(i,j)] = randint(0,1)
#for i in range(dimensao):
#    for j in range(dimensao):
#        print(f'[{d[(i,j)]:^5}]', end = ' ')
#    print()
#print('Trocar a segunda linha, pela terceira ->')
#for j in range(dimensao-1):
#    d[(1,j)], d[(2,j)] = d[(2,j)], d[(1,j)]
#for i in range(dimensao):
#    for j in range(dimensao):
#        print(f'[{d[(i,j)]}]', end = '')
#    print()

#from random import randint
#matriz = {(i,j): randint(1,5) for i in range(4) for j in range(4)}
#for i in range(4):
#    for j in range(4):
#        print(f'[{matriz[(i,j)]}]', end = '')
#    print()
#medias = []
#for i in range(4):
#    soma  = sum(matriz[(i,j)] for j in range(4))
#    media = soma/4
#    medias.append(media)
#print(f'médias -> {medias}')

