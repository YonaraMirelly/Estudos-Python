# ler uma frase e colocá-la ao contrário e dizer se ela é um palíndromo
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1 ,-1):
    inverso += junto[letra]
print('A frase {} ao contrário é {}.'.format(frase, inverso))
if inverso == junto:
    print('\033[1;32mSIM\033[m, sua frase é um palíndromo.')
else:
    print('Sua frase \033[1;31mNÃO\033[m é um palíndromo.')
input()
