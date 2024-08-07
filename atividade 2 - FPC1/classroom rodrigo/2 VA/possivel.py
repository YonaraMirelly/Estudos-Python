
class Pilha:
    def __init__(self):
        self.items = []

    def vazia(self):
        return self.items == []

    def empilhar(self, item):
        self.items.append(item)

    def desempilhar(self):
        return self.items.pop()

    def topo(self):
        return self.items[-1]

def avaliar_expressao(expressao):
    pilha = Pilha()
    for caractere in expressao:
        if caractere.isdigit():
            pilha.empilhar(int(caractere))
        elif caractere in "+-*/":
            operando2 = pilha.desempilhar()
            operando1 = pilha.desempilhar()
            if caractere == "+":
                resultado = operando1 + operando2
            elif caractere == "-":
                resultado = operando1 - operando2
            elif caractere == "*":
                resultado = operando1 * operando2
            elif caractere == "/":
                resultado = operando1 / operando2
            pilha.empilhar(resultado)
        elif caractere == "(":
            pilha.empilhar(caractere)
        elif caractere == ")":
            subexpressao = ""
            while pilha.topo() != "(":
                subexpressao = pilha.desempilhar() + subexpressao
            pilha.desempilhar()  # Remove o "("
            pilha.empilhar(avaliar_expressao(subexpressao))
    return pilha.desempilhar()

expressao = "{2+1[3*3-(2-1)]+4}"
expressao_sem_chaves = "".join(c for c in expressao if c not in "{}[]")  # Remover chaves e colchetes
resultado = avaliar_expressao(expressao_sem_chaves)
print("Resultado da expressão:", resultado)
