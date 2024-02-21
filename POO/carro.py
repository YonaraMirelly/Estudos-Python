class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0

    def andar(self, distancia):
        consumo_total = distancia / self.consumo
        if consumo_total <= self.combustivel:
            self.combustivel -= consumo_total
        else:
            print("Combustível insuficiente para percorrer a distância.")

    def obterGasolina(self):
        return self.combustivel

    def adicionarGasolina(self, quantidade):
        self.combustivel += quantidade

# Testando a classe
meuFusca = Carro(15)  # 15 quilômetros por litro de combustível.
meuFusca.adicionarGasolina(20)  # abastece com 20 litros de combustível.
meuFusca.andar(100)  # anda 100 quilômetros.
print(f"Combustível restante: {meuFusca.obterGasolina()} litros")  # Imprime o combustível que resta no tanque.
