class Livro:
    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor
    
    def alugar(self):
        if self.alugado:
            print('Livro já está alugado')
        else:
            self.alugado = True
            print("Livro foi alugado com sucesso!")

    def devolver(self):
        if self.alugado:
            self.alugado = False
            print('O livro foi devolvido.')
        else:
            print('O livro não está alugado.')


class Biblioteca:
    def __init__(self):
        self.lista_disponiveis = []
        self.lista_alugaods = []

    def AdicionarLivro(self, livro):
        self.lista_disponiveis.append(livro)

    def AlugarLivro(self, titulo):
        for livro in self.lista_disponiveis:
            if livro.titulo == titulo:
                livro.alugar()
                self.lista_disponiveis.remove(livro)
                self.lista_alugaods.append(livro)
                return
        print('O livro não está disponível na biblioteca.')

    def Devolver_livro(self, titulo):
        for livro in self.lista_alugaods:
            if livro.titulo == titulo:
                livro.devolver()

