#with open('tt.txt', 'w') as file:
#    file.write(input('escreva -> '))
#    file.close()
#file = open('tt.txt', 'r')
#ler = file.read()
#print(ler)

#d = {}
#with open('teste.txt', 'r') as file:
#    linhas = file.readlines()
#    for linha in linhas:
#        chave, elemento = linha.strip().split(' ')
#        d[chave] = elemento
#print(d)
#file.close()


#def validar(ip):
#    ip = ip.split('.')
#    for elemento in ip:
#        if not 0<= int(elemento) <=254:
#            return False
#        return True
#with open('teste.txt', 'r') as file:
#    linhas = file.readlines()
#    for linha in linhas:
#        j = linha.strip()
#        if validar(j):
#            print(f'{j} é válido')
#        else:
#            print(f'{j} é inválido')

#with open('teste.txt', 'r') as file:
#    linhas = file.readlines()
#novos_nomes = sorted([linha.strip() for linha in linhas])
#file.close()
#with open('novos_nomes.txt', 'w') as file:
#    for nome in novos_nomes:
#        file.write(nome + '\n')
#ile.close()
#with open('novos_nomes.txt', 'r') as file:
#    ler = file.read()
#print(ler)

#with open('teste.txt', 'r') as file:
#    linhas = file.readlines()
#linhas_sele = linhas[2:5]
#with open('novo.txt', 'w') as file:
#    for linha in linhas_sele:
#        file.write(linha)
#file.close()
#with open('novo.txt', 'r') as file:
#    ler = file.read()
#print(ler)

#arq = input('diga o nome do arquivo -> ')
#qL = 0
#qP = 0
#with open(arq, 'r') as file:
#    linhas = file.readlines()
#    for linha in linhas:
#        qL +=1
#        if 'print' in linha:
#            qP+=1
#print(f'tem {qL} linhas')
#print(f'tem {qP} prints no seu arquivo!')
