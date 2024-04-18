def fatorial_iterativo(n):
    result = 1
    for i in range(1, n+1):
        result *=i
    return result
print(fatorial_iterativo(5))
    