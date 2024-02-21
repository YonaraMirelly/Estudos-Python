arquivo = input()
qtde_linhas = 0
qtde_print = 0

with open(arquivo, 'r') as file:
    linhas = file.readlines()
    for linha in linhas:
        qtde_linhas+=1
        if 'print' in linha:
            qtde_print+=1

print(qtde_linhas)
print(qtde_print)