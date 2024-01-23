#ler 6 números inteiros e mostrar a soma dos números pares.
soma = 0
count = 0
for n in range(1,7):
    n = int(input('Digite o {}ª número: '.format(n)))
    if n % 2 == 0:
        soma += n
        count += 1
print('Você informou {} números pares e a soma é igual a {}.'.format(count, soma))
input()