class No:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None

class Pilha:
    def __init__(self):
        self.topo = None

    def isVazia(self):
        return self.topo is None

    def inserir(self, valor):
        novo_no = No(valor)
        novo_no.prox = self.topo
        self.topo = novo_no

    def remover_topo(self):
        if self.isVazia():
            return None
        valor = self.topo.valor
        self.topo = self.topo.prox
        return valor

    def topo_valor(self):
        if self.isVazia():
            return None
        return self.topo.valor

def calculadora (expressao):
    pilha = Pilha()
    operadores = expressao.split()

    for operador in reversed(operadores):
        if operador.isdigit():
            pilha.inserir(int(operador))
        else:
            if pilha.isVazia():
                return "Expressão inválida"
            n2 = pilha.remover_topo()
            if pilha.isVazia():
                return "Expressão inválida"
            n1 = pilha.remover_topo()
            if operador == '+':
                resultado = n2 + n1
            elif operador == '-':
                resultado = n2 - n1
            elif operador == '*':
                resultado = n2 * n1
            elif operador == '/':
                resultado = int(n2 / n1)  
            pilha.inserir(resultado)

    if pilha.isVazia() or pilha.topo.prox is not None:
        return "Expressão inválida"
    else:
        return pilha.remover_topo()

entrada = [
    "* 199 - + 725 148 + 902 885",
    "+ - + 879 608 842 - - 251 43 906",
    "- 484 390",
    "+ 635 + + 114 927 557",
    "- 224 - + 18 309 - 620 683",
    "+ + + 403 408 - 917 853 + + 568 791 + 692 322",
    "/ + 162 661 + 2 + 932 6",
    "/ + - 837 35 - 332 124 - - 260 605 - 751 463",
    "/ + 376 - 466 399 + * 310 707 378",
    "- 782 197"
]

for expressao in entrada:
    resultado = calculadora (expressao)
    print(resultado)
