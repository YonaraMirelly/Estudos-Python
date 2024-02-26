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

