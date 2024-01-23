lista = []
menor = 0
maior = 0
for numero in range(0, 5):
    lista.append(int(input('Digite um valor para a posição {}: '.format(numero))))
    if numero == 0:
        maior = menor = lista[numero]
    else:
        if lista[numero] > maior:
            maior = lista[numero]
        if lista[numero] < menor:
            menor = lista[numero]
print('-='*30)
print(f'Você digitou os valores {lista}')
print(f'O MAIOR valor digitado foi {maior} nas posições ', end = '')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}... ', end = '')
print(f'\nO MENOR valor digitado foi {menor} nas posições ', end = '')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ', end = '')
input()