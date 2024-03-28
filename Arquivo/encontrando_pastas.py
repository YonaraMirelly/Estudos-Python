import os
arquivos = os.listdir(os.getcwd()+"//noticias/")
print(arquivos)
nome = str(input("Digite alguma palavra a ser encontrada dentro das notícias: "))
for arquivo in arquivos:
    with open(os.getcwd()+"//noticias/"+arquivo, 'r') as file:
        conteudo = file.read()
        if nome in conteudo.split(' '):
            print(f'\033[1;36m{nome}\033[m foi encontrado no arquivo {arquivo} {conteudo.count(nome)} vezes.')
        else:
            print(f'\033[1;36m{nome}\033[m \033[1;31mNÃO\033[m foi encontrado no arquivo {arquivo}')