#s1 = str(input('string1- '))
#s2 = str(input('string2 - '))
#print(f'comprimento {s1} = {len(s1)}')
#print(f'comprimento {s2} = {len(s2)}')
#if len(s1) == len(s2):
#    print('têm o mesmo comprimento')
#else:
#    print('não têm o mesmo comprimento')
#if s1 == s2:
#    print('literalmente idênticas.')

#def String(s1,s2):
#    print(f'comprimento de {s1} = {len(s1)}')
#    print(f'comprimento de {s2} = {len(s2)}')
#    if len(s1) == len(s2):
#        print('têm o mesmo comprimento')
#    else:
#        print('não tem o mesmo comprimento')
#    if s1 == s2:
#        print('idênticos!')
#String('yona', 'yonar')

#nome = str(input('nome: '))
#novo = nome[::-1].upper()
#print(novo)

#def Nome(nome):
#    novo = nome[::-1].upper()
#    print(novo)
#Nome('yonara')

#nome = str(input('nome - '))
#for letra in nome:
#    print(letra)

#nome = str(input('nome - '))
#for i in range(len(nome)+1):
#    print(nome[:i])

#def Maneiro(nome):
#    for i in range(len(nome)+1):
#        print(nome[:i])
#Maneiro('poly')

#s = str(input('frase: '))
#print(s.count('ado'))  

#dna = str(input('sequência -> ')).upper()
#rna = ''
#for letra in dna:
#    if letra == "A":
#        rna +="U"
#    elif letra == 'G':
#        rna +="C"
#    elif letra == 'C':
#        rna +="G"
#    elif letra == "T":
#        rna +="A"
#print(rna)

#def Transformar(dna):
#    rna = ''
#    for letra in dna:
#        if letra == 'a':
#            rna+="u"
#        elif letra == "g":
#            rna+="c"
#        elif letra == "c":
#            rna +="g"
#        elif letra == "t":
#            rna +="a"
#    
#    print(rna.upper())
#Transformar('agct')

from random import randint
print("joguinho")
cont = 0
pc = randint(1,3)
while True:
    j = int(input('numero -> '))
    cont +=1
    if j > pc:
        print(f'um pouco menos')
    elif j < pc:
        print(f'um pouco mais')
    elif j == pc:
        break
print(f'Você acertou com {cont} tentativas...')
print(f'voce digitou {j} e o pc tbm digitou {pc}!!')