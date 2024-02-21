class Conta:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        novo = self.saldo + valor
        return novo
    
    def saque(self, saque):
        if self.saldo >= saque:
            self.saldo -=saque
        else:
            print("Saldo insuficiente.")

    def exibir_saldo(self):
        print(f'Saldo R${self.saldo}')

class ContaCorrente(Conta):
    def __init__(self, saldo, taxa):
        super().__init__(saldo)
        self.taxa = taxa

    def desconto(self):
        self.saldo -= self.taxa

class Poupança(Conta):
    def __init__(self, saldo, rendimento):
        super().__init__(saldo)
        self.rendimento = rendimento
    
    def Rendimento(self):
        self.saldo *= (1 + self.rendimento /100)

class ContaImposto(Conta):
    def __init__(self, saldo, imposto):
        super().__init__(saldo)
        self.imposto = imposto

    def CalculaImposto(self):
        imposto = self.saldo * (self.imposto/100)
        return imposto
    
contacorrente = ContaCorrente(1000, 10)
contapoupança = Poupança(2000, 2)
conta_imposto = ContaImposto(3000, 5)

print(contacorrente.depositar(500))
print(contacorrente.desconto())
print(contacorrente.exibir_saldo())

print(contapoupança.Rendimento())
print(contapoupança.exibir_saldo())

print(conta_imposto.CalculaImposto())
print(conta_imposto.exibir_saldo())