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



