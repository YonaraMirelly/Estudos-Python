#n = int(input('Digite um número para calcular o seu fatorial: '))
#f = 1
#print('Calculando {}! = '.format(n), end='')
#for i in range(n, 0 ,-1):
#    print(i,end='')
#    f = f * i
#    print(' x ' if i >1 else ' = ', end='')
#print('{}'.format(f))
#input()

#def fat(n):
 #   if n<2:
 #       return 1
 #   else:
 #       return n * fat(n-1)
    
#fat(5)

def fib(n):
    if n <=2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(30))