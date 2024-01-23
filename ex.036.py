#saber o valor da casa, salário do comprador e em quanto tempo ele quer pagar
casa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o valor do seu salário? R$'))
anos = float(input('Em quantos anos você planeja pagar? '))
#calcular o valor da prestação mensal
p = anos * 12
p1 = casa // p
porcentagem = (30 * salario) / 100
#condição: não pode excerder 30% do valor do salário.
if p1 <= porcentagem:
    print('Para pagar uma casa de R${}, Você terá que pagar R${:.2f} por mês em {} anos.\nEMPRÉSTIMO PERMITIDO'.format(casa, p1, anos))
else:
    print('Para pagar uma casa de R${}, você terá que pagar R${:.2f} por mês em {} anos.\nEMPRÉSTIMO NEGADO.'.format(casa, p1, anos))
input()
