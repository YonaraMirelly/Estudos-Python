totalpessoas18 = totalhomem = totalmulher20 = 0
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo: [F/M] ')).strip().upper()[0]
    if idade >= 18:
        totalpessoas18 +=1
    if sexo == 'M':
        totalhomem +=1
    if sexo == 'F' and idade < 20:
        totalmulher20 +=1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {totalpessoas18}')
print(f'Ao todo, temos {totalhomem} homens acadastrados.')
print(f'E temos {totalmulher20} mulheres com menos de 20 anos.')
        