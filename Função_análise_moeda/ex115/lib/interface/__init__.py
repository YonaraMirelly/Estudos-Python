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

def linha(tam = 42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[1;33m{c}\033[m - \033[1;34m{item}\033[m')
        c +=1
    print(linha())
    opc = leiaint('\033[1;32mSua opção:\033[m ')
    return opc