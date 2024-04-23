### Primeira Questão -> 
# def Comb_recursivo(n,k):
#     if k == 1:
#         return n
#     elif k == n:
#         return 1
#     elif 1< k <n:
#         return Comb_recursivo(n-1, k-1) + Comb_recursivo(n-1, k)
# print(Comb_recursivo(5,3))
# def Comb_nao(n,k):
#     if k ==0 or k==n:
#         return 1
#     result = 1
#     for i in range(1, k+1):
#         result *= (n-i+1)
#         result //=i
#     return result
# print(Comb_nao(5,3))

### Segunda Questão -> 
# def Maior(v, i=0, maior=0):
#     if i == len(v):
#         return maior
#     else:
#         if v[i] > maior:
#             maior = v[i]
#         return Maior(v, i+1, maior)

# print(Maior([99,2,3000,18,990])) ok
# def F(n):
#     if n < 4:
#         return 3 * n
#     else:
#         return 2*F(n-4)+5
# print(F(7))
# print(F(3)) ok

## Terceira Questão ->
# def RaizQ(x, xo, e):
#     if (xo**2)-x <= e:
#         return xo
#     else:
#         return RaizQ(x, (xo**2 + x) / 2*xo, e)

# print(RaizQ(13, 3.5, 0.001))

### Quarta Questão -> 
# def A(m, n):
#     if m == 0:
#         return n + 1
#     elif m >0 and n == 0:
#         return A(m-1, 1)
#     elif m>0 and n>0:
#         return A(m-1, A(m, n-1))

# print(A(1,2)) ok

### Sexta Questão -> 
# def f(x,n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return x
#     else:
#         return x * f(x, n-1)
# print(f(2, 3))
# print(f(5, 2))

### Sétima Questão -> 
# def fat(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * fat(n-1)
# print(fat(5))

# def Permutaçao(v, p = ''):
#     if len(v) == 1:
#         print(p + v[0])
#     else:
#         for indice, simbolo in enumerate(v):
#             restante = v[:indice] + v[indice+1:]
#             Permutaçao(restante, p+simbolo)
#     return ''

# print(Permutaçao(['a', 'b', 'c']))

### Oitava questão ->
# def placar(m, n, prox=''):
#     if m ==0 and n ==0:
#         print(prox)
#         return ''
#     if m > 0:
#         placar(m-1, n, prox + "A")
#     if n > 0:
#         placar(m, n-1, prox + "B")
    
# print(placar(3, 1))

### Nona questão ->
# def calcula(x, n):
#     if n == 1:
#         return x
#     else:
#         return x + calcula(x, n-1)
# print(calcula(2,5))

### Décima questão ->
# def soma(array, i=0):
#     if i == len(array):
#         return 0
#     else:
#         return array[i] + soma(array, i+1)
    
# print(soma([1,2,3]))

### 11 ->
# def inverter(array, i=0, nova=[]):
#     if i < len(array):
#         inverter(array, i+1, nova)
#         nova += [array[i]]
#     return nova
# print(inverter([1, 2, 3]))

### 12 ->
# def qtde(k, numero):
#     if numero == 0:
#         return 0
#     ultimo_digito = numero % 10
#     if ultimo_digito == k:
#         return 1 + qtde(k , numero // 10)
#     else:
#         return qtde(k , numero // 10)
    
# print(qtde(2, 120))

### 13 -> 
# def binario(n):
#     if n == 0:
#         return '0'
#     elif n == 1:
#         return '1'
#     else:
#         binarios = binario(n//2)
#         return binarios + str(n%2)
# print(binario(5))

### 14 -> 
# def mdc(x, y):
#     if y == x:
#         return x
#     if x == 0:
#         return y
#     if y == 0:
#         return x
#     if x>y:
#         return mdc(x-y, y)
#     else:
#         return mdc(y,x)

# print(mdc(6, 3))

### 15 ->
# def resto(x, y):
#     if x == y:
#         return 0
#     elif x < y:
#         return x
#     elif x>y:
#         return resto(x-y, y)

# print(resto(17, 2))

### 16 -> 
# def ad(array, array2):
#     if not array:
#         return array2
#     if not array2:
#         return array
#     if array[0] in array2:
#         array2.remove(array[0])
#     return [array[0]] + ad(array[1:], array2)

# print(ad([1,1], [2,2]))

### 17 ->
# def conjunto(l):
#     if not l:
#         return [[]]
#     else:
#         elemento = l[0]
#         resto = conjunto(l[1:])
#     return resto + [[elemento]+ subconjunto for subconjunto in resto]

# print(conjunto(['a', 'b', 'c']))