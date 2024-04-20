# def maior(lista, nmax, i):
#     if i == len(lista):
#         return nmax
#     if lista[i] > nmax:
#         nmax = lista[i]
#     return maior(lista, nmax, i+1)

# num = [int(i) for i in input().split()]
# print(maior(num, 0, 0))

# def maior(a, i):
#     if i == len(a)-1:
#         return a[i]
#     maior_resto = maior(a, i+1)
#     if a[i] > maior_resto:
#         maior_resto =  a[i]
#     return maior_resto

# print(maior('123', 0))
def main(x, y):
    result = 1
    for _ in range(y):
        result *= x
    return result

if __name__ == "__main__":
    x, y = [float(i) for i in input().split()]
    y = int(y)
    result = main(x, y)
    print(f"{result:.4f}")

