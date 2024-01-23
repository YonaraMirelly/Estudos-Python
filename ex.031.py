distancia = float(input('Qual foi a distância percorrida durante a viagem? '))
menor = distancia * 0.50
maior = distancia * 0.45
if distancia <200:
    print('O total da passagem é \033[1;32mR${:.2f}\033[m.'.format(menor))
else:
    print('O total da passagem é \033[1;32mR${:.2f}\033[m.'.format(maior))
input()