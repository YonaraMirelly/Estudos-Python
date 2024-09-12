# entrada do usuario
lin_fazenda, col_fazenda, lin_caju, col_caju = [int(i) for i in input().split()]
fazenda = []

def meu_max(a, b):
    if a > b:
        return a
    else:
        return b
# leitura dos números de cajus
for _ in range(col_fazenda):
    x = [int(i) for i in input().split()]
    fazenda.append(x)

max_produtividade = 0  # variavel para guardar valor e comparar depois
for i in range(lin_fazenda - lin_caju + 1):
    for j in range(col_fazenda - col_caju + 1):  # percorrendo a matriz grande
        area = 0  # guarda o valor de soma atual da matriz pequena e reinicia sempre que começa outra matriz
        for linha in range(i, lin_caju + i):
            for coluna in range(j, col_caju + j):  # percorrendo pela pequena matriz de cajus possiveis
                area += fazenda[linha][coluna]
        max_produtividade = meu_max(max_produtividade, area)  # comparando o maior valor entre o atual e o armazenado


print(max_produtividade)  # imprimindo o resultado na tela