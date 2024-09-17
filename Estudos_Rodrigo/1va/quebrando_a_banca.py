# ok
def Apagar_menor(): #O(1)
    casos = [] #O(1)
    while True: #O(n)
        entrada = input('A e B -> ') #O(1)
        if entrada == '': #O(1)
            break #O(1)
        else:
            L = entrada.split() #O(1)
            listaAB = [int(i) for i in L] #O(1)
            digitos = [int(i) for i in input('Número a ser analisado -> ')] #O(1)
            for i in range(listaAB[-1]):  #O(n)
                c = 100 #O(1)
                for j in digitos:  #O(n)
                    if j < c: #O(1)
                        c = j #O(1)a
                digitos.remove(c)  #O(n)
            casos += [digitos]  #O(n)
    for caso in casos:  #O(n) 
        for x in caso:  #O(n)
            print(x, end = '') #O(1)
        print() #O(1)
Apagar_menor()


