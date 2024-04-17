# def Comb_recursivo(n,k):
#     if k == 1:
#         return n
#     elif k == n:
#         return 1
#     elif 1< k <n:
#         return Comb_recursivo(n-1, k-1) + Comb_recursivo(n-1, k)
# print(Comb_recursivo(4,3))

def Comb_nao(n,k):
    if k ==0 or k==n:
        return 1
    result = 1
    for i in range(1, k+1):
        result *= (n-i+1)
        result //=i
    return result

print(Comb_nao(4,3))