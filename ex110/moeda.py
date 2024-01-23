def aumentar(pr = 0,t = 0, formato = False):
    res = pr + (pr * t/100)
    return res if not formato else moeda(res)


def diminuir(pr = 0,t = 0, formato = False):
    res = pr -(pr * t/100)
    return res if not formato else moeda(res)


def dobro(pr = 0, formato = False):
    res = pr *2
    return res if not formato else moeda(res)


def metade(pr = 0, formato = False):
    res = pr/2
    return res if not formato else moeda(res)

def moeda(pr = 0, moeda = 'R$'):
    return f'{moeda}{pr:.2f}'.replace('.', ',')


def resumo(pr = 0, taxaa = 10, taxar = 5 ):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t\033[1;32m{moeda(pr)}\033[m')
    print(f'Dobro do preço: \t{dobro(pr, True)}')
    print(f'Metade do preço: \t{metade(pr, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(pr, taxaa, True)}')
    print(f'{taxar}% de redução: \t\t{diminuir(pr, taxar, True)}')
    print('-'*30)