nome = 'yonara'
def laço(nome, inicio = 0, fim = 0):
    if inicio < len(nome):
        if fim < len(nome):
            print(nome[inicio:fim+1])
            laço(nome, inicio, fim+1)
        else:
            laço(nome, inicio+1, inicio+1)

print(laço(nome))