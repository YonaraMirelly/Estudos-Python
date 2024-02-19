d = {}
d2 = {}
while True:
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    cpf = str(input("CPF: "))
    d[cpf] = {'nome': nome, 'idade': idade, 'cpf': cpf}
    resp = str(input("Deseja adicionar + alguém? [S/N] ")).upper()
    print('-'*20)
    if resp == "N":
        if d[cpf]['idade'] <18:
            d1 = d.copy()
            d2 = d1.pop(cpf)
            print(f'Aqui pessoas menores de 18: {d2}')
            print(f'Aqui temos o dicionario sem pessoas menores de 18 anos: {d}')


    

        