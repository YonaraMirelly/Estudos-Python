with open('texto.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

linhas_selecionadas = linhas[2:5]

with open('linhas_selecionadas', 'w') as arquivo:
    for linhas in linhas_selecionadas:
        arquivo.write(linhas)