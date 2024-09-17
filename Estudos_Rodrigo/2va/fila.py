
class No:
    def __init__(self, dado=None):
        self.dado = dado
        self.prox = None
        self.ant = None

    def __str__(self):
        return f"Dado: {self.dado}"

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def esta_vazia(self):
        return self.inicio is None or self.fim is None

    def inserir(self, dado):
        novo_no = No(dado)
        if self.esta_vazia():
            self.inicio = novo_no
            self.fim = novo_no
        else:
            novo_no.ant = self.fim
            self.fim.prox = novo_no
            self.fim = novo_no

    def remover(self):
        if self.esta_vazia():
            return None

        dado = self.inicio.dado
        if self.inicio == self.fim:
            self.inicio = None
            self.fim = None
        else:
            self.inicio = self.inicio.prox
            self.inicio.ant = None

        return dado

    def imprimir(self):
        atual = self.inicio
        while atual:
            print(atual.dado, end=" ")
            atual = atual.prox
        print()

def main():
    N = int(input())
    fila_inicial = list(map(int, input().split()))

    M = int(input())
    pessoas_que_sairam = set(map(int, input().split()))

    minha_fila = Fila()

    for pessoa in fila_inicial:
        minha_fila.inserir(pessoa)

    for pessoa in pessoas_que_sairam:
        no_atual = minha_fila.inicio
        while no_atual:
            if no_atual.dado == pessoa:
                if no_atual == minha_fila.inicio:
                    minha_fila.remover()
                elif no_atual == minha_fila.fim:
                    minha_fila.fim = no_atual.ant
                    no_atual.ant.prox = None
                else:
                    no_atual.ant.prox = no_atual.prox
                    no_atual.prox.ant = no_atual.ant
                break
            no_atual = no_atual.prox

    minha_fila.imprimir()

main()