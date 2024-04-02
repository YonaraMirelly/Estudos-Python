#p = 'roletrando'
#y = '----------'
#print(y)
#v = 5
#w = 0
#lg = ''
#while v!=0 and w != 10:
#    n = ''
#    c = input('chute uma letra -> ')
#    z = 0
#    for i in range(10):
#        if c == p[i]:
#            n +=p[i]
#            z = 1
#            w +=1
#        elif y[i] == p[i]:
#            n +=p[i]
#        else:
#            n += "_"
#    y = n
#    if z == 0:
#        v-=1
#    lg +=c+''
#    print(n)
#    print(f'Letras Gastas -> {lg}')
#    print(f'Vidas Restantes -> {v}')
#if v == 0:
#    print(f'Você perdeu! A palavra era {p}')
#else:
#    print(f'Você Ganhou! A palavra é {p}!')
op = ''
lista = []
while True:
    nome = input('nome: ')
    lista.append(nome)
    op = input('quer adicionar mais algum nome?[N/S] ').upper()
    if op == "N":
        break
for nome in lista:
    for i in range(len(nome)+1):
        print(nome[:i])
        print('-'*10)
