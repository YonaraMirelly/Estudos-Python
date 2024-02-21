class Atleta:
    def __init__(self, nome , idade):
        self.nome = nome
        self.idade = idade
    def aposentar(self):
        if self.idade >60:
            return f'{self.nome} Deve aposentar'
        else:
            return f'Não aposentar'

    def aquecer(self):
        return 'aquecendo'
    
class Corredor(Atleta):
    def correr(self):
        return f'{self.nome} está correndo'
    
class Nadador(Atleta):
    def nadar(self):
        return f'{self.nome} está nadando'
    
class Ciclista(Atleta):
    def pedalar(self):
        return f'{self.nome} está pedalando'
    
class Tri(Corredor, Nadador, Ciclista):
    pass

tri = Tri('yonara', 19)
print(tri.aposentar())
print(tri.nadar())
print(tri.aquecer())
print(tri.correr())
print(tri.pedalar())