class Funcionario:
    nome = None
    salario = None
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def AumentarSalario(self, percentual):
        aumento = self.salario * (percentual/100)
        self.salario += aumento

harry = Funcionario("harry", 100)
harry.AumentarSalario(10)
print(f'Salário aumentado-> {harry.salario}')
