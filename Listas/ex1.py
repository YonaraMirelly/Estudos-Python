#l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

#print(l[1:9])
#print(l[8:13])

#par = [x for x in l if x%2==0]
#print(f'lista par - {par}')
#impar = [x for x in l if x%2!=0]
#print(f'lista impar = {impar}')

#multidois = [x for x in l if x%2==0]
#multitres = [x for x in l if x%3==0]
#multiquatro = [x for x in l if x%4==0]
#print(f'multiplo de 2 = {multidois}')
#print(f'multiplo de 3 = {multitres}')
#print(f'multiplo de 4 = {multiquatro}')

#print(l[::-1])
#dez = sum(l[10:15])
#tres = sum(l[3:9])
#razao = float(dez/tres)
#print(f'razão é {razao}')

#l = [1,2,3,4,5]
#for i, e in enumerate(l):
#    print(f'No índice {i} está {e}')

#l = [1,2,3,4,5,6,7,8,9,10]
#print(l[::-1])

#def Inverso(l):
#    print(l[::-1])
#Inverso([1,2,3,4,5])

#l = []
#for i in range(4):
#    n = int(input(f'digite a {i+1} nota -> '))
#    l.append(n)
#soma = sum(l)
#media = soma/4
#for elemento in l:
#    print(elemento, end = ' / ')
#print(f'a média é {media}')


#lista = [31,44,55,77,1]
#maior = menor = lista[0]
#for elemento in lista:
#    if elemento > maior:
#        maior = elemento
#    elif elemento<menor:
#        menor = elemento    
#print(f'maior - {maior}')
#print(f'menor - {menor}')

#def Maior(lista):
#    maior = menor = lista[0]
#    for elemento in lista:
#        if elemento > maior:
#            maior = elemento
#        elif elemento < menor:
#            menor = elemento
#    print(f'maior - {maior}')
#    print(f'menor - {menor}')
#Maior([1,2,3,4,5])

#lista = [1,2,3,4,5]
#par = [x for x in lista if x%2==0]
#impar = [x for x in lista if x%2!=0]
#print(f'par - {par}')
#print(f'impar - {impar}')

#def Par(lista):
#    par = [x for x in lista if x%2==0]
#    impar = [x for x in lista if x%2!=0]
#    print(f'par - {par}')
#    print(f'impar = {impar}')
#Par([10,23,24,25,26])

#temperaturas = []
#meses = ['janeiro', 'fevereiro', 'março', 'abril', "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
#for mes in meses:
#    t = float(input(f'{mes} -> '))
#    temperaturas.append(t)
#soma = sum(temperaturas)
#media = soma/12
#print(f'a média é {media:.2f}')
#print('temperatuta acima da média anual->')
#for i, temperatura in enumerate(temperaturas):
#    if temperatura> media:
#        print(f'{meses[i]} -> {temperatura}°C')

#from random import randint
#m = []
#dimensao = int(input('dimensão -> '))
#for i in range(dimensao):
#    nova_linha = []
#    for j in range(dimensao):
#        elemento = randint(1,10)
#        nova_linha.append(elemento)
#    m.append(nova_linha)
#for i in range(dimensao):
#    for j in range(dimensao):
#        print(f'[{m[i][j]:^5}]', end = '')
#    print()
#print('='*40)
#print('dobro')
#for i in range(dimensao):
#    for j in range(dimensao):
#        print(f'[{m[i][j]*2:^5}]', end = '')
#    print()


#cont = 0
#lista = []
#while True:
#    nota = float(input('nota -> '))
#    cont+=1
#    lista.append(nota)
#    op = input('quer continuar? [S/N] ')
#    if op == "N":
#        break
#    else:
#        continue    
#print(f'quantas notas -> {cont}')
#print(f'informadas -> {lista}')
#print('inversa: ')
#inversa = lista[::-1]
#for elemento in inversa:
#    print(elemento)
#soma = sum(lista)
#media = soma/cont
#print(f'soma = {soma}')
#print(f'média = {media}')
#for elemento in lista:
#    if elemento > media:
#        print(f'maior que a média: {elemento}')

#lista = []
#n = input('Telefonou para a vítima? ').upper()
#n1 = input('Esteve no local do crime? ').upper()
#n2 = input('Mora perto da vítima? ').upper()
#n3 = input('Tínha dívidas com a vítima? ').upper()
#n4 = input('já trabalhou com a vítima? ').upper()
#lista.append(n)
#lista.append(n1)
#lista.append(n2)
#lista.append(n3)
#lista.append(n4)
#if lista.count('SIM') == 2:
#    print('você é suspeito')
#elif 3<= lista.count('SIM') <= 4:
#    print('você é cúmplice')
#if lista.count('SIM') == 5:
#    print('Assasino!')


#tot = 0
#votos = []
#while True:
#    print('''
#1 - windows
#2 - unix
#3 - linux
#4 - netware
#5 - mac
#6 - outro''')
#    voto = int(input('Voto -> '))
#    if voto > 6 or voto < 0:
#        print('digite um número válido!')
#    elif voto == 0:
#        break
#    else:
#        votos.append(voto)
#tot = len(votos)
#window = votos.count(1)
#unix = votos.count(2)
#linux = votos.count(3)
#netware = votos.count(4)
#mac = votos.count(5)
#outro = votos.count(6)
#percW = window/tot*100
#percU = unix/tot*100
#percL = linux/tot*100
#percN = netware/tot*100
#percM = mac/tot*100
#perO = outro/tot*100
#print(f'{tot} pessoas votaram!')
#print(f'Windows -> {percW:.2f}%')
#print(f'unix -> {percU:.2f}%')
#print(f'linux -> {percL:.2f}%')
#print(f'netware -> {percN:.2f}%')
#print(f'mac -> {percM:.2f}%')
#print(f'outro -> {perO:.2f}%')
#nomes = ['windows', 'unix', 'linux', 'netware', 'mac', 'outro']
#porcentagens = [percW, percU, percL, percN, percM, perO]
#maior_porcentagem = max(porcentagens)
#indice = porcentagens.index(maior_porcentagem)
#print(f'{nomes[indice]} ganhou com {maior_porcentagem}%!!!!!!!!!!!!!!!!!!!!!!!')

from random import randint
matriz = []

for l in range(3):
    novalinha = []
    for c in range(3):
        elemento = randint(1,3)
        novalinha.append(elemento)
    matriz.append(novalinha)

for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:9.2f}]', end = '')
    print()

print('trocando a segunda linha, pela terceira')

matriz[1], matriz[0] = matriz[0], matriz[1]

for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:9.2f}]', end = '')
    print()

print('trocando a primeira coluna pela terceira')
for l in range(3):
    matriz[l][0], matriz[l][2] = matriz[l][2], matriz[l][0]

for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:9.2f}]', end = '')
    print()