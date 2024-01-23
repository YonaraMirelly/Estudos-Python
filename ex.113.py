def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! POR FAVOR DIGITE UM NÚMERO INTEIRO VÁLIDO.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[1;31mO USUÁRIO RESOLVEU NÃO DIGITAR O VALOR.\033[m')
            return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! POR FAVOR DIGITE UM NÚMERO DECIMAL.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[1;31mO USUÁRIO RESOLVEU NÃO DIGITAR O NÚMERO.\033[m')
            return 0
        else:
            return n
        

num = leiaint('Digite um número inteiro: ')
num2 = leiafloat('Digite um número decimal: ')
print(f'O valor inteiro foi {num} e o valor decimal foi {num2}')


    
                
