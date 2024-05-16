def cesar(palavra, deslocamento):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    cifra = alfabeto[-deslocamento:] + alfabeto[:-deslocamento]
    palavra_cifrada = ''
    for letra in palavra:
        indice = alfabeto.index(letra.lower())
        cifrada = cifra[indice]
        palavra_cifrada += cifrada
    
    nova_lista = [palavra_cifrada]
    for j in nova_lista:
        print(j, end=' ')

def principal():
    texto = [str(i) for i in input('Texto: ').split()]
    deslocamento = int(input('Dale o Deslocamento - '))
    
    for palavra in texto:
        cesar(palavra, deslocamento)

principal()
    