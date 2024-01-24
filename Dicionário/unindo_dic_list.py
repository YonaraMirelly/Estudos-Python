galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input(f'Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! POR FAVOR DIGITE APENAS M OU F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! RESPONDA APENAS S OU N.')
    if resp == 'N':
        break
print('=-'*20)
print(galera)
print(f'A) Ao todo foram {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idades é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram: ', end= ' ')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end = ' ')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('    ', end = '')
        for k, v in p.items():
            print(f'{k} = {v}; ', end = '')
        print()
print('>> ENCERRADO <<')
input()
