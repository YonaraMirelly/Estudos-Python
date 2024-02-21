with open('nomes.txt', 'r') as arquivo:
    nomes = arquivo.readlines()

nomes_ordenados = sorted([nome.strip() for nome in nomes])

with open('nomes_ordenados.txt','w') as arquivo:
    for nome in nomes_ordenados:
        arquivo.write(nome + '\n')
