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
