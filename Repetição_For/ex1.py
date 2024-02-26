#representantes = 10
#for i in range(representantes):
#    itens = int(input(f'Itens de {i+1} '))
#    valor_total = float(input(f'Valor total de {i+1} '))
#    if itens < 19:
#        comissao = valor_total * 0.1
#    elif itens < 49:
#        comissao = valor_total * 0.15
#    elif itens < 74:
#        comissao = valor_total * 0.2
#    else:
#        comissao = valor_total * 0.25    
#    print(f'Da fábrida {i+1} comissão de R${comissao:.2f}')

#def Comissao(representante):
#    for i in range(representante):
#        iten = int(input('iten: '))
#        valor =  float(input('valor: '))
#        if iten < 19:
#            comissao = valor * 0.1
#        elif 20 < iten < 49:
#            comissao = valor * 0.15
#        elif 50 < iten < 74:
#            comissao = valor * 0.2
#        else:
#            comissao = valor * 0.25
#        print(f'Fabrida {i+1} recebe de comissão R$ {comissao}')
#Comissao(10)

#maior = menor = soma = N_homens = N_mulher = media =   0
#sexo_mais_alta = ''
#for i in range(1, 4):
#    sexo = str(input('sexo [F/M] -> '))
#    altura = float(input('altura -> '))
#    if i == 1:
#        maior = menor = altura
#        sexo_mais_alta = sexo
#    else:
#        if altura > maior:
#            maior = altura
#            sexo_mais_alta = sexo
#        elif altura < menor:
#            menor  = altura
#        
#        if sexo == "F":
#            soma += altura
#            N_mulher +=1
#        elif sexo == "M":
#            N_homens +=1
#media  = soma / N_mulher
#print(f'Maior altura -> {maior}')
#print(f'Menor altura -> {menor}')
#print(f'Número de homens -> {N_homens}')
#print(f'Sexo da pessoa mais alta -> {sexo_mais_alta}')
#print(f'Média das mulheres -> {media}')

#def Pessoas(qtde):
#    maior = menor = media = N_homem = N_mulher = soma= 0
#    sexo_mais_alto = ''
#    for i in range(qtde):
#        sexo = str(input('sexo [F/M] '))
#        altura = float(input('altura '))
#        if i == 0:
#            maior  = menor = altura
#            sexo_mais_alto = sexo
#        else:
#            if altura > maior:
#                maior = altura
#                sexo_mais_alto = sexo
#            elif altura < menor:
#                menor = altura
#            if sexo == "F":
#                soma += altura
#                N_mulher +=1
#            elif sexo == "M":
#                N_homem+=1
#    media = soma / N_mulher
#    print(f'Maior altura -> {maior}')
#    print(f'Menor altura -> {menor}')
#    print(f'Número de homens -> {N_homem}')
#    print(f'Sexo da pessoa mais alta -> {sexo_mais_alto}')
#    print(f'Média das mulheres -> {media}')
#Pessoas(3)

#totA = totB = totC = tot_nulo = tot_branco = TOTAL = 0
#for i in range(16):
#    print("""1 - A
#2 - B
#3 - C
#4 - Nulo
#5 - Branco
#""")
#    voto = int(input('Seu voto -> '))
#    if voto == 1:
#       totA +=1
#    elif voto ==2:
#        totB +=1
#    elif voto ==3:
#        totC +=1
#    elif voto ==4:
#        tot_nulo+=1
#    elif voto ==5:
#        tot_branco+=1
#    else:
#        print('voto inválido')
#    TOTAL +=1
#pn = tot_nulo/TOTAL
#pb = tot_branco / TOTAL
#print(f'Total pra A: {totA}')
#print(f'Total pra B: {totB}')
#print(f'Total pra c: {totC}')
#print(f'Total pra nulo: {tot_nulo}')
#print(f'Total pra branco: {tot_branco}')
#print(f'percentual de nulo: {pn*100}%')
#print(f'percentual de branco: {pb*100}%')


#par = 0
#impar = 0
#for i in range (11):
#    n = int(input('número -> '))
#    if n %2 == 0:
#        par +=1
#    else:
#        impar +=1
#print(f'qtde_pares {par}')
#print(f'qtde_impar {impar}')

#def Par(qtde):
#    par = impar = 0
#    for i in range(qtde):
#        n = int(input('número -> '))
#        if n %2 == 0:
#            par +=1
#        else:
#print(f'maior - {maior}')
#print(f'menor - {menor}')
#print(f'media - {media}')


#def Temperatura(n):
#    maior = menor = media = soma = total = 0
#    for i in range(n):
#        t = float(input('temperatura - '))
#        if i == 0:
#            maior = menor = t
#        else:
#            if t>maior:
#                maior = t
#            elif t<menor:
#                menor = t
#        total +=1
#        soma +=t
#    media = soma/total 
#    print(f'maior = {maior}')
#    print(f'menor = {menor}')
#    print(f'média = {media}')
#Temperatura(2)
