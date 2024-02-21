class Produto:
    qtde = 0
    def __init__(self, codigo, preço):
        self._codigo = codigo
        self._preço = preço
        Produto.qtde +=1

    def getpreço(self):
        return self._preço
    
    def setpreço(self, valor):
        novo = self._preço = valor
        return novo
        
    
a = Produto('1', 10)
b = Produto('2', 20)
print(f'quantidade de pessoas-> {Produto.qtde}')
print(f'Preço do produto A-> {a.getpreço()}')
print(f'Preço do produto b-> {b.getpreço()}')
print(f'Novo valor de A-> {a.setpreço(50)}')
