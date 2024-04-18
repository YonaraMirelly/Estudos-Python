### Primeira Questão -> 
# def Comb_recursivo(n,k):
#     if k == 1:
#         return n
#     elif k == n:
#         return 1
#     elif 1< k <n:
#         return Comb_recursivo(n-1, k-1) + Comb_recursivo(n-1, k)
# print(Comb_recursivo(4,3))
# def Comb_nao(n,k):
#     if k ==0 or k==n:
#         return 1
#     result = 1
#     for i in range(1, k+1):
#         result *= (n-i+1)
#         result //=i
#     return result
# print(Comb_nao(4,3))

### Segunda Questão -> 
# def F(n):
#     if n < 4:
#         return 3 * n
#     else:
#         return 2*F(n-4)+5
    
# print(F(3))

## Terceira Questão ->
def RaizQ(x, xo, e):
    if (xo**2)-x <= e:
        return xo
    else:
        return RaizQ(x, (xo**2 + x) / 2*xo, e)

print(RaizQ(13, 3.5, 0.001))

### Quarta Questão -> 
# def A(m, n):
#     if m == 0:
#         return n + 1
#     elif m >0 and n == 0:
#         return A(m-1, 1)
#     elif m>0 and n>0:
#         return A(m-1, A(m, n-1))

# print(A(1,2))

### Sexta Questão -> 
# def f(x,n):
#     if n == 0:
#         return 1
#     elif n % 2 == 0:
#         temp = f(x, n//2)
#         return temp * temp
#     else:
#         temp = f(x, (n-1)//2)
#         return x * temp * temp
    
# print(f(5, 2))

### Sétima Questão -> 
