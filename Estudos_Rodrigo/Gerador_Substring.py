


# print('Com 2 laços -> ')
# nome = str(input('nome: '))
# for i in range(len(nome)):
#     for j in range(i+1, len(nome)+1):
#         print(nome[i:j])

# print('Com 1 laço ->')
# nome = str(input('nome: '))
# i = j = 0
# while True:
#     j += 1
#     print(nome[i:j], end = ' ')
#     if j == len(nome):
#         i += 1
#     if i == len(nome) and j == len(nome):
#         print(nome[i+1:j], end = ' ')
#         break
#     if j > len(nome):
#         j = 0

print('Sem laço -> ')
def Sem_laço(nome, inicio=0, fim=0):
    if inicio < len(nome):
        if fim < len(nome):
            print(nome[inicio:fim+1])
            Sem_laço(nome, inicio, fim+1)
        else:
            Sem_laço(nome, inicio+1, inicio+1)

nome = str(input('Nome > '))
Sem_laço(nome)