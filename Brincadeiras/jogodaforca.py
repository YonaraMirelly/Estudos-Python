palavra = 'PYTHON'
letra_palavra = list(palavra)
palavra_exibida = ['_'] * len(palavra)

max = 6

tentativas = 0

letras_tentadas = []

while palavra_exibida != palavra and tentativas<max:
    print(f'A palavra é {' '.join(palavra_exibida)}')

    letra = input('Digite uma letra ->').upper()

    if letra in letras_tentadas:
        print('Você já tentou essa letra!')
        continue
    
    letras_tentadas.append(letra)

    if letra in letra_palavra:
        print('você acertou!')
        for i, l in enumerate(letra_palavra):
            if l == letra:
                palavra_exibida[i] = letra
    
    else:
        print('você errou')
        tentativas+=1
        
if palavra_exibida == letra_palavra:
    print('Parabéns, você adivinhou!')
else:
    print(f'você errou! a palavra era ')