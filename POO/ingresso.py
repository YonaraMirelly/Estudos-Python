class Ingresso:
    def __init__(self,valor):
        self.valor = valor

    def ImprimeValor(self):
        return self.valor
    

class VIP(Ingresso):
    def __init__(self, valor, valor_adicional):
        super().__init__(valor)
        self.valor_adicional = valor_adicional

    def adicionar(self):
        return self.valor + self.valor_adicional
    
ingresso = Ingresso(50)
vip = VIP(50,30)

print(ingresso.ImprimeValor())
print(f'Ingresso VIP-> {vip.adicionar():.2f}')