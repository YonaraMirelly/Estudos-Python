from time import sleep
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
escolha = 0
while escolha != 5:
    print('Escolha uma das opções abaixo:')
    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] NOVOS NÚMEROS')
    print('[5] SAIR DO PROGRAMA')
    escolha = int(input('Qual é sua escolha? '))
    if escolha == 1:
        print('A soma entre {} e {} é igual a {}.'.format(n1,n2, n1 + n2))
    elif escolha == 2:
        print('O resultado da multiplicação entre {} e {} é {}.'.format(n1,n2, n1 * n2))
    elif escolha == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {}, o maior é {}.'.format(n1,n2, maior))
    elif escolha == 4:
        print('Digite números novos...')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif escolha == 5:
        print('Finalizando....')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 20)
    sleep(2)
print('Fim do programa, volte sempre!')
input()

        
            
        
      
   


