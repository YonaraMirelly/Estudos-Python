def exponencial_modular(a, n, m):
    if n == 0:
        if a == 0:
            return "impossível calcular"
        return 1
    if m <=1:
        return 'impossível calcular'
    return a * exponencial_modular(a, n-1, m)

a, n, m = [int(i) for i in input().split()]
resultado = exponencial_modular(a, n, m)
if type(resultado) == int:
    print(resultado%m)
else:
    print(resultado)