entrada = [int(i) for i in input().split()]
lista_geral = []
qtde_k = 0
qtde_v = 0
for i in range(entrada[0]):
    lista_geral += [str(j) for j in input()]

for x in lista_geral:
    if x == 'k':
        qtde_k += 1
    if x == 'v':
        qtde_v +=1

if qtde_v > qtde_k:
    diminuir = qtde_v - qtde_k
    qtde_k -= diminuir
    print(qtde_k, qtde_v)

if qtde_k > qtde_v:
    diminuir = qtde_k - qtde_v
    qtde_v -= diminuir
    qtde_k -= diminuir
    print(qtde_v, qtde_k)
