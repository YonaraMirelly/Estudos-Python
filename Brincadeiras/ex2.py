#L = [12,14,15]
#A = [x**3 for x in L if x%2 ==0]
#B = [(x%10)**2 for x in L]
#print(A)
#print(B)

#def Inicializa():
#    mat = [[0,0,0], [0,0,0], [0,0,0]]
#    mat[1][1] = 10
#    return mat
#m = Inicializa()
#def Imprime(matriz):
#    for l in range(3):
#        for c in range(3):
#            print(f'[{m[l][c]:7.1f}]', end = '')
#        print()
#m = Imprime([[0,0,0], [0,0,0], [0,0,0]])

#print('JOGO DA VELHA')
#print('Jogadores -> O X')
#jogador = ''
#while jogador == '':
#    jogador = input('Escolha o jogador que vai começar -> ')
#    if jogador != 'O' and jogador != 'X':
#        print('erro, tente novamente')
#        jogador = ''

#a = 0
#b = 1
#numero = int(input('digite até que numero a sequencia irá -> '))
#while a < numero:
#    print(a, end = ' - ')
#    a, b = b, a+b

#def Fibonacci(n):
#    ultimo = 1
#    penultimo = 0
#    novo = 1
#    if n == 1:
#        return penultimo
#    elif n == 2:
#        return ultimo
#    elif n>2:
#        for _ in range(n-2):
#            novo = ultimo+penultimo
#            penultimo = ultimo
#            ultimo = novo
#        return novo
#print(Fibonacci(13))

#qtde = int(input('quantas pessoas -> '))
#dic = {}
#for i in range(qtde):
#    print(f'dados da pessoa {i+1} -->')
#    nome = str(input('nome -> '))
#    idade = int(input('idade -> '))
#    tel = str(input('telefone -> '))
#    end = str(input('endereço -> '))
#    cpf = str(input('CPF -> '))
#    dic[cpf] = {'nome': nome, 'idade': idade, 'telefone': tel, 'endereço': end, 'cpf': cpf}
#for cpf, pessoa in dic.items():
#    if pessoa['idade'] >=18:
#        print(f'{cpf} -> {pessoa['nome']}')

#linha = int(input('linha -> '))
#coluna = int(input('coluna -> '))
#matriz = []
#for l in range(linha):
#    novalinha = []
#    for c in range(coluna):
#        numero = float(input(f'digite para [{l+1, c+1}] -> '))
#        novalinha.append(numero)
#    matriz.append(novalinha)
#print('ela normal -> ')
#for l in range(linha):
#    for c in range(coluna):
#        print(f'[{matriz[l][c]:9.2f}]', end = '')
#    print()
#print('vezes 3 -> ')
#for l in range(linha):
#    for c in range(coluna):
#        print(f'[{matriz[l][c]*3:9.2f}]', end = '')
#    print()

#n = int(input('você quer o fatorial de -> '))
#f = 1
#c = n
#while c>0:
#    print(f'{c}', end = '')
#    print(f' x ' if c>1 else ' = ', end = '')
#    f*=c
#    c-=1
#print(f'{f}')

#x = int(input('digite o numero de x ->'))
#fat = 1
#resp = 1
#for i in range(1,51):
#    fat *=i
#    resp += (x**i)/fat
#print(resp)

#nome = 'Isabel Cristina Leopoldina Augusta Micaela Gabriela Rafaela Gonzaga de Bragança e Bourbón'
#nome_sem_leo = nome.split('Leopoldina ')
#junto1 = ''.join(nome_sem_leo)
#nome_sem_Gonza = junto1.split('Gonzaga ')
#junto2 = ''.join(nome_sem_Gonza)
#print(junto2)

#idades = []
#maior = 0
#menor = 1000

#for i in range(3):
#    idades.append(int(input('idade -> ')))
#for i in idades:
#    if i > maior:
#        maior = i
#    if i < menor:
#        menor = i

#print(f'maior {maior}')
#print(f'menor {menor}')

#def Fatorialwhile(n):
#    resultado = 1
#    i = 2
#    while i < (n+1):
#        resultado  *= i
#        i+=1
#    return resultado

#d = Fatorialwhile(5)
#print(d)