funcionarios = {}

for i in range(3):
    nome = str(input(f'Funcionário {i+1}: '))
    funcionarios[i+1] = nome

print(f'Lista de Funcionários: {funcionarios}')

num = int(input('Digite o número do funcionário que você quer demitir: '))
funcionarios.pop(num)

print(f'Funcionários atualizados: {funcionarios}')