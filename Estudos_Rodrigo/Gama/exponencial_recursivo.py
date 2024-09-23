def exp(a, n):
    if n == 0:
        if a == 0:
            return "impossível calcular"
        return 1
    return a * exp(a, n-1)

a, n = [int(i) for i in input().split()]
print(exp(a, n))