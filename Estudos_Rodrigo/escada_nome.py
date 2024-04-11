# nome = str(input('Nome:'))
# print('Com for -> ')
# for i in range(len(nome)+1):
#     print(nome[:i])


# print('Com for -> ')
# nome = str(input('nome: '))
# for i in range(len(nome)):
#     for j in range(i+1, len(nome)+1):
#         print(nome[i:j])

# print('Com while ->')
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

def um_laço(s):
    for inicio in range(len(s)):
        substring(s, inicio, inicio+1)
    
def substring(s, inicio, fim):
    if fim <= len(s):
        print(s[inicio:fim])
        substring(s, inicio, fim+1)
        
def principal():
    s = "heloisa"
    um_laço(s)
      
if __name__ == "__main__":
    principal()
