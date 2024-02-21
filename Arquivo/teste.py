arq = open('teste.txt', 'r')

linhas = arq.readlines()

dic = {}

for linha in linhas:
    chave, elemento = linha.strip().split(' ')

    dic[chave] = elemento

print(dic)

arq.close()