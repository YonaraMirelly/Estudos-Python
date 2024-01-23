num = float(input('Qual o salário do funcionário? R$'))
aumento1 = num * 1.1
aumento2 = num * 1.15
if num >= 1250:
    print('Seu salário atual é \033[7;32;45m{}\033[m, com o aumento, seu salário é \033[1;32mR${:.2f}\033[m'.format(num, aumento1))
else:
    print('Seu salário atual é \033[7;32;45m{}\033[m, com o aumento, seu salário é \033[1;32mR${:.2f}\033[m'.format(num, aumento2))
input()
