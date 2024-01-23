def aumentar(pr = 0,t = 0):
    res = pr + (pr * t/100)
    return res


def diminuir(pr = 0,t = 0):
    res = pr -(pr * t/100)
    return res


def dobro(pr = 0):
    res = pr *2
    return res


def metade(pr = 0):
    res = pr/2
    return res

def moeda(pr = 0, moeda = 'R$'):
    return f'{moeda}{pr:.2f}'.replace('.', ',')



