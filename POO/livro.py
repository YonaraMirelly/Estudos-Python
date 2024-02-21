class Livro:
    def __init__(self, nome, qtde_paginas, autor, preço):
        self.nome = nome
        self.qtde_paginas = qtde_paginas
        self.autor = autor
        self.preço = preço
    
    def getPreço(self):
        return self.preço
    
    def setPreço(self, valor):
        novo = self.preço = valor
        return novo


livro = Livro('mar', 100, 'yonara', 90.00)
print(f'Preço-> {livro.getPreço()}')
print(f'Novo preço-> {livro.setPreço(50.00)}')