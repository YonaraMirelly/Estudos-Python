class No:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None

class Pilha:
    def __init__(self):
        self.prox = None
        self.tamanho = 0

    def isVazia(self):
        return self.tamanho == 0

    def inserir(self, dado):
        novo_no = No(dado)
        novo_no.anterior = self.prox
        self.prox = novo_no
        self.tamanho += 1

    def remover(self):
        if self.isVazia():
            return None
        no_removido = self.prox
        self.prox = self.prox.anterior
        self.tamanho -= 1
        return no_removido.dado

    def buscar(self):
        if self.isVazia():
            return None
        return self.prox.dado

resultado = []
T = int(input())

for i in range (T):
    A = input()
    pilha = Pilha()
    for j in A:
        if j == ')' or j == ']' or j == '}':
            if j == ')' and pilha.buscar() == '(':
                pilha.remover()
            elif j == ']' and pilha.buscar() == '[':
                pilha.remover()
            elif j == '}' and pilha.buscar() == '{':
                pilha.remover()
            else:
                pilha.inserir(j)
        else:
            pilha.inserir(j)
    
    if pilha.isVazia():
        resultado.append('S')
    else:
        resultado.append('N')

for i in range (len(resultado)):
    print(resultado[i])

            



