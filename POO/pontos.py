class Ponto:
    def __init__(self, nome, x, y):
        self.nome = nome
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'{self.nome} -> {self.x} {self.y}'
    

ponto1 = Ponto('A', 100, 200)
ponto2 = Ponto('B', 130, 150)
ponto3 = Ponto('C', 500, 239)
outro = Ponto('outroponto', 199, 54)

lista = [ponto1,ponto2,ponto3,outro]

for elemento in lista:
    print(elemento)