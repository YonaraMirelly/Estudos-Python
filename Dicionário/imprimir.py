#Faça um programa, utilizando Dicionários, 
#que peça para o usuário inserir quatro notas e mostre na tela as notas e a média entre elas.

nota1 = float(input('primeira nota: '))
nota2 = float(input('segunda nota: '))
nota3 = float(input('terceira nota: '))
nota4 = float(input('quarta nota: '))

dic = {
    'nota1': nota1,
    'nota2': nota2,
    'nota3': nota3,
    'nota4': nota4,
}
media = (nota1 + nota2 + nota3+ nota4) / 4
print(dic)
print(media)