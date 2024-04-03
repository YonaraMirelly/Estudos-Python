total = int(input())
n = int(input())
if 1 <= total <= 100 and 1 <= n <=300:
    lista = [i for i in range(1, total +1)]
    contador = 0
    for _ in range(n):
        figurinha = int(input('dale -> '))
        if figurinha in lista:
            lista.remove(figurinha)
            contador += 1
    falta = total - contador
    print(falta)
else:
    print('Digite valores positivos e dentro dos requisitos, por favor!')