dic = {}
dic['nome'] = str(input('nome: '))
dic['media'] = float(input(f'média de {dic["nome"]}: '))
if dic['media'] >= 7:
    dic['situação'] = 'Aprovado'
elif 5 <= dic['media'] <7:
    dic['situação'] = 'Recuperação'
else:
    dic['situação'] = 'Reprovado'
print('='*40)
for k, v in dic.items():
    print(f'O {k} é igual a {v}.')
input()