def Maior():
    casos = []
    while True:
        entrada = input('A e B -> ')
        if entrada == '':
            break
        else:
            L = entrada.split()
            listaAB = [int(i) for i in L]
            digitos = [int(i) for i in input('Número a ser analisado -> ')]
            limite = listaAB[0] - listaAB[-1]
            c = 0
            lista_Geral = [None] * limite
            for i in range(limite):
                c = 0
                for j in digitos:
                    if j > c:
                        c = j
                        lista_Geral[i] = c
                digitos.remove(c)
            numero = ''
            for i in lista_Geral:
                numero+=str(i)
            casos += [numero]
            numero = ''
    
    for x in casos:
        print(x)

Maior()