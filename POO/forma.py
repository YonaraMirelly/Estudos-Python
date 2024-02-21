class Forma:
    def __init__(self):
        self.area = 0
        self.perimetro = 0
        
class Retangulo(Forma):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b
    def CalculaArea(self):
      self.area = self.a * self.b
      return self.area

    def CalculaPerimetro(self):
        self.area = 2* (self.a + self.b)
        return self.area

class Triangulo(Forma):
    def __init__(self, base, altura, lado_c):
        super().__init__()
        self.base = base
        self.altura = altura
        self.lado_c = lado_c
    def CalculaArea(self):
        self.area = self.base * self.altura /2
        return self.area

    def CalculaPerimetro(self):
        self.perimetro = self.base + self.altura + self.lado_c
        return self.perimetro

triangulo = Triangulo(2,4,3)
retangulo = Retangulo(1,2)

print(triangulo.CalculaArea())
print(triangulo.CalculaPerimetro())
print(retangulo.CalculaArea())
print(retangulo.CalculaPerimetro()) 