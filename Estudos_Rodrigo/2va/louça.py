# atividade 17
class No:
    def __init__(self, dado=None):
        self.dado = str(dado)
        self.prox = None
        self.ant = None

    def __str__(self):
        return f"O dado é {self.dado}"


class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def isvazia(self):
        if self.inicio is None:
            return True
        else:
            return False

    def inserir_no_inicio(self, dado):
        novo_no = No(dado)
        if self.isvazia():
            self.inicio = novo_no
        else:
            novo_no.prox = self.inicio
            self.inicio.ant = novo_no
            self.inicio = novo_no

    def buscar(self, x):
        i = self.inicio
        while i is not None:
            if x == i.dado:
                break
            i = i.prox
        return i

    def remover(self, x):
        noencontrado = self.buscar(x)
        if noencontrado is not None:
            if noencontrado.ant is not None:
                noencontrado.ant.prox = noencontrado.prox
            else:
                self.inicio = noencontrado.prox
            if noencontrado.prox is not None:
                noencontrado.prox.ant = noencontrado.ant
            else:
                self.fim = noencontrado.ant
        return noencontrado

    def inserir_no_fim(self, dado=None):
        novono = No(dado)
        if self.isvazia():
            self.inicio = self.fim = novono
        else:
            novono.ant = self.fim
            self.fim.prox = novono
            self.fim = novono

    def __str__(self):
        s = ''
        i = self.inicio
        while i is not None:
            s += f"{str(i)} "
            i = i.prox
        return s


class Fila(Lista):
    def remover_do_inicio(self):
        if not self.isvazia():
            if self.inicio.prox is None:
                self.fim = None
            else:
                self.inicio.prox.ant = None
            self.inicio = self.inicio.prox

    def comparar_cartas(self, carta):
        if str(self.inicio) == str(carta.inicio):
            carta.remover_do_inicio()
        else:
            carta.inserir_no_fim(carta.inicio.dado)
            carta.remover_do_inicio()


def main():
    qtd_festa = int(input())

    for _ in range(qtd_festa):
        cartas_mesa = list(map(int, input().split()))
        lista_temporaria = cartas_mesa.copy()
        cartas_mesa = Fila()
        for j in lista_temporaria:
            cartas_mesa.inserir_no_fim(j)

        qtd_jogadores = 0
        cartas_dos_convidados = []

        while True:
            convidado_atual = list(map(int, input().split()))
            if convidado_atual[0] != -1:
                cartas_convidado = Fila()
                for j in convidado_atual:
                    cartas_convidado.inserir_no_fim(j)
                cartas_dos_convidados.append(cartas_convidado)
                qtd_jogadores += 1
            else:
                break

        qtd_rodadas = 0
        ganhador = None

        while qtd_rodadas < 1000:
            qtd_rodadas += 1

            for i in range(qtd_jogadores):
                cartas_mesa.comparar_cartas(cartas_dos_convidados[i])
                if cartas_dos_convidados[i].isvazia():
                    ganhador = i + 1
                    break

            if ganhador is not None:
                break

            cartas_mesa.inserir_no_fim(cartas_mesa.inicio.dado)
            cartas_mesa.remover_do_inicio()

        if ganhador is None:
            print(0)
        else:
            print(ganhador)


if __name__ == "__main__":
    main()