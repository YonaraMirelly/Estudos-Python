def Apagar_menor():
    casos = []
    while True:
        entrada = input('A e B -> ')
        if entrada == '':
            break
        else:
            L = entrada.split()
            listaAB = [int(i) for i in L]
            digitos = [int(i) for i in input('Número a ser analisado -> ')]
            for i in range(listaAB[-1]):
                c = 100
                for j in digitos:
                    if j < c:
                        c = j
                digitos.remove(c)
            casos += [digitos]
    for caso in casos:
        for x in caso:
            print(x, end = '')
        print()
Apagar_menor()


