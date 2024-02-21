class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c
    
    def CalcularPerimetro(self):
        return self.lado_a + self.lado_b + self.lado_c
    
    def CalcularArea(self):
        return self.lado_a * self.lado_b / 2
    
    def GetMaiorLado(self, ):
        if self.lado_a > self.lado_b and self.lado_a > self.lado_c:
            return self.lado_a
        elif self.lado_b > self.lado_a and self.lado_b > self.lado_c:
            return self.lado_b
        else:
            return self.lado_c
    
lado_a = int(input("Lado base: "))
lado_b = int(input("Lado altura: "))
lado_c = int(input("Lado diagonal: "))

triangulo = Triangulo(lado_a, lado_b, lado_c)
print(f"Perímetro-> {triangulo.CalcularPerimetro()}")
print(f'Area-> {triangulo.CalcularArea()}')
print(f"maior lado-> {triangulo.GetMaiorLado()}")