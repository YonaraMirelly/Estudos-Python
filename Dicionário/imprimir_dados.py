

quantidade = int(input("Digite a quantidade de pessoas: "))
pessoas = {}
pessoas_dic = {}

for i in range(quantidade):
    nome = str(input(f"Nome {i+1}: "))
    idade = int(input(f"Idade {i+1}: "))
    tel = str(input(f"Telefone {i+1}: "))
    end = str(input(f"Endereço {i+1}: "))
    cpf = str(input(f"CPF {i+1}: "))
    print("-"*10)
    pessoas[cpf] = [nome, idade, tel, end] 

    pessoas_dic[cpf] = {'nome':nome, 'idade':idade, 'telefone': tel,'endereço': end}

sair = False
while not sair:
    busca = str(input("Você que os dados de qual cpf? "))
    if busca in pessoas_dic:
        print(f'Dados de {pessoas_dic[busca]['nome']} : {pessoas[busca]}')
    else:
        print("Pessoa não encontrada.")

    rep = str(input("Deseja encontrar outra pessoa? ")).upper()
    if rep == 'NÃO' or rep =='N':
        sair = True

print("Finalizando... Fim :)")
