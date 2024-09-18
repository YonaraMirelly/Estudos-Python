class No:
    def __init__(self, inicio, fim, altura):
        self.inicio = inicio
        self.fim = fim
        self.altura = altura
        self.anterior = None

class Pilha:
    def __init__(self):
        self.proximo = None  # Representa o topo da pilha
        self.tamanho = 0     # Tamanho da pilha

    def is_vazia(self):
        return self.tamanho == 0  # Verifica se a pilha está vazia

    def inserir(self, inicio, fim, altura):
        novo_no = No(inicio, fim, altura)
        novo_no.anterior = self.proximo  # Aponta o novo nó para o atual topo
        self.proximo = novo_no           # Atualiza o topo da pilha
        self.tamanho += 1                # Incrementa o tamanho da pilha

    def remover(self):
        if self.is_vazia():
            return None  # Se a pilha está vazia, retorna None

        no_removido = self.proximo        # Guarda o nó do topo
        self.proximo = self.proximo.anterior  # Move o topo para o próximo nó
        self.tamanho -= 1                 # Decrementa o tamanho da pilha
        return no_removido                # Retorna o nó removido


def marcação_de_regua_pilha(N, H):
    marcas = [' ' for _ in range(N + 1)]
    pilha = Pilha()

    # Empilha o estado inicial
    pilha.inserir(0, N, H)

    # Enquanto a pilha não estiver vazia
    while not pilha.is_vazia():
        no_atual = pilha.remover()
        inicio = no_atual.inicio
        fim = no_atual.fim
        altura = no_atual.altura

        if altura == 0:
            continue

        meio = (inicio + fim) // 2
        marcas[meio] = '-' * altura

        # Empilha os dois subintervalos (esquerda e direita)
        pilha.inserir(meio, fim, altura - 1)   # Lado direito
        pilha.inserir(inicio, meio, altura - 1)  # Lado esquerdo

    return marcas


# Exemplo de uso
N, H = [int(x) for x in input().split()]
marcas = marcação_de_regua_pilha(N, H)

for i in range(N+1):
    print(f' {i}{marcas[i]} ')
