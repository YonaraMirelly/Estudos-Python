#Crie um programa que tenha uma tupla única com nomes de produtos 
#e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, 
#organizando os dados em forma tabular.
lista = ('Minecraft', 300, 'GTA-SanAndreas', 200, 'Fifa', 60, 'Spider-man', 50, 'The Last of Us', 550, 'GTA V', 675.99, 'Super Mario', 30, 'Terraria', 10.33, 'God of War', 1000.20)
print('='*40)
print(f'{"LISTA DE PREÇO DE JOGOS":^40}')
print('='*40)
for pos in range(0, len(lista)):
    if pos % 2 ==0:
        print(f'{lista[pos]:.<30}', end = '')
    else:
        print(f'R${lista[pos]:>7.2f}')
input()