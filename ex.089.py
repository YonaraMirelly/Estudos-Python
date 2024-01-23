ficha = []

escolha = 'Ss'
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2] , media])
    escolha = str(input('Quer continuar? [S/N] '))
    if escolha in 'Nn':
        break
print('-='*30)
print(f'{"Nª":<4}{"NOME":<10}{"MÉDIA":<9}' )
print('-'*25)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:<9}')
while True:
    print('=-'*30)
    opçao = int(input('Mostrar notas de qual aluno? [999 interrompe] ')) 
    if opçao == 999:
        print('FINALIZANDO...')
        break
    if opçao <= len(ficha)-1:
        print(f'Notas de {ficha[opçao][0]} são {ficha[opçao][1]}.')
print('VOLTE SEMPRE >)')

