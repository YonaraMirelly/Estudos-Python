# Definição das classes e métodos
class No:
    def __init__(self, elemento):
        self.elemento = elemento
        self.proximo = None
        self.anterior = None

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def inserir(self, elemento, posicao=False):
        novo_no = No(elemento)
        if self.inicio is None and self.fim is None:
            self.inicio = novo_no        
            self.fim = novo_no
        else:
            if posicao is False:
                self.fim.proximo = novo_no
                novo_no.anterior = self.fim
                self.fim = novo_no
            else:
                inicio = self.inicio
                for i in range(posicao):
                    inicio = inicio.proximo
                novo_no.proximo = inicio
                inicio.anterior = novo_no
                novo_no.anterior = inicio.anterior
                inicio.anterior.proximo = novo_no

    def __str__(self):
        no_atual = self.inicio
        string = ""
        while no_atual is not None:
            string += str(no_atual.elemento) + " "
            no_atual = no_atual.proximo
        return string

# Criando uma lista duplamente encadeada
lista = ListaDuplamenteEncadeada()

# Inserindo elementos na lista
lista.inserir(1)  # Insere no fim
lista.inserir(2, 0)  # Insere no início
lista.inserir(3, 1)  # Insere na posição 1
lista.inserir(4)  # Insere no fim

# Imprimindo a lista
print(lista)
