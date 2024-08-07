# ok
r1 = [int(i) for i in input().split()] #O(1)
r2 = [int(i) for i in input().split()] #O(1)
if r1[-1] and r1[-2] > r2[0] and r2[1] or r1 == r2: #O(n)
    print(1) #O(1)
elif r2[-1] and r2[-2] > r1[0] and r1[1]: #O(n)
    print(1) #O(1)
else:
    print(0) #O(1)

# esse algoritmo tem uma complexidade linear, pois o tempo de execução cresce linearmente
# com o tamanho da lista de entrada.