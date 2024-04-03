tamanho = int(input("Informe qntd de fig "))
lista = list(range(1, tamanho + 1))

figsCompradas = int(input("Quantas figs compradas?"))

contador = 0
for x in range(figsCompradas):
    fig = int(input("Qual comprou "))
    if fig in lista:
        lista.remove(fig)
        contador += 1

restantes = tamanho - contador
print(restantes)