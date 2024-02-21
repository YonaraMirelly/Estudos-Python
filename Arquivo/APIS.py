


def validar(ip):
    ip = ip.split('.')
    for elem in ip:
        if not 0 <= int(elem) <= 254:
            return False
        return True
 
with open('API.txt', 'r') as file:
    linhas = file.readlines()
    for linha in linhas:
        j= linha.strip()
        if validar(j):
            print(j, 'Válido')
        else:
            print(j, 'Inválido')

