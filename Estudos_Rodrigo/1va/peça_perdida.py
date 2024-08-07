# ok
n = int(input()) #O(1)
incompleta = [int(i) for i in input().split()] #O(n)
# vA fórmula para calcular a soma dos n 
# primeiros números naturais é uma operação constante, independentemente do valor de n.
soma_completa = int(n * (n + 1) /2 ) #O(1)
soma_incompleta = 0 #O(1)
"""O loop for itera sobre cada elemento da lista incompleta, 
realizando uma adição a cada iteração. Portanto, essa parte tem complexidade linear O(n).
"""
for i in incompleta: #O(n)
    soma_incompleta += i #O(n)
falta = soma_completa - soma_incompleta #O(1)
print(falta) #O(1)

