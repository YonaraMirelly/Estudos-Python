#from random import randint
#class Matriz:
#    dic = None
#    tamanho = None
#    def __init__(self):
#        self.dic = {}
#        self.tamanho = 0
#    def __init__(self, matriz, tamanho):
#        self.dic = matriz
#        self.tamanho = tamanho
#    def Imprime(self):
#        for i in range(self.tamanho):
#            for j in range(self.tamanho):
#                print(f'[{self.dic[(i,j)]:^5}]', end = '')
#            print()
#matriz = {(i,j) : randint(0,1) for i in range(4) for j in range(4)}
#m = Matriz(matriz,4)
#print(m.Imprime())

#class Triangulo:
#    def __init__(self, a, b , c):
#        self.a = a
#        self.b = b
#        self.c = c
#    def Perimetro(self):
#        return self.a + self.b + self.c
#    def Maior(self):
#        if self.a > self.b and self.a > self.c:
#            maior = self.a
#        elif self.b> self.c and self.b>self.a:
#            maior = self.b
#        elif self.c> self.a and self.c>self.b:
#            maior =  self.c
#        return maior
#triangulo = Triangulo(1,2,3)
#print(triangulo.Maior())

#class Funcionario:
#    def __init__(self, nome, salario):
#        self.nome = nome
#        self.salario = salario
#    def Aumentar(self, taxa):
#        aumento = self.salario * (taxa/100)
#        novo = self.salario + aumento
#        return f'R${novo}'
#hary = Funcionario('harry', 50)
#print(hary.Aumentar(50))

#class Livro:
#    def __init__(self, nome, qtde, autor, preço):
#        self.nome = nome
#        self.qtde = qtde
#        self.autor = autor
#        self.preço = preço
#    def Get(self):
#        return self.preço
#    def Set(self, valor):
#        novo = self.preço + valor
#        return novo
#livro = Livro('mar', 50, 'eu', 100)
#print(livro.Set(90))

#class Aluno:
#    def __init__(self, nome, curso, tempo_sem_dormir):
#        self.nome = nome
#        self.curso = curso
#        self.tempo = tempo_sem_dormir
#    def Estudar(self, qtde_horas_estudo):
#        self.tempo += qtde_horas_estudo
#        return self.tempo
#    def Dormir(self, qtde_horas_sono):
#        self.tempo -= qtde_horas_sono
#        return self.tempo
#aluno = Aluno('yonara', 'SI', 16)
#print(f'Tempo estuando -> {aluno.Estudar(8)}')
#print(f'Tempo dormindo -> {aluno.Dormir(5)}')

#class Carro:
#    def __init__(self, consumo):
#        self.consumo = consumo
#        self.combustivel = 0
#    def Andar(self, distancia):
#        consumo_total = distancia/self.consumo
#        if consumo_total<=self.combustivel:
#            self.combustivel-=consumo_total
#        else:
#            print('combustivel insuficiente!')
#    def Obter(self):
#        return self.combustivel
#    def Adicionar(self, gasolina):
#        self.combustivel+=gasolina
#fusca = Carro(15)
#fusca.Adicionar(20)
#fusca.Andar(100)
#print(f'Combustível restante é {fusca.Obter():.2f}')

#class Aluno:
#    def __init__(self, nome, cpf):
#        self.nome = nome
#        self.cpf = cpf
#class Equipe:
#    def __init__(self, participante, projeto):
#        self.participantes = participante
#        self.projeto = projeto
#class Gerenciador:
#    def __init__(self):
#        self.equipes = []
#    def Criar(self, alunos, projeto):
#        for equipe in self.equipes:
#            if equipe.projeto == projeto:
#                for aluno in alunos:
#                    for participante in equipe.participantes:
#                        if aluno.cpf == participante.cpf:
#                            print('já tem aluno nesse projeto!')
#                            return
#        nova_equipe = Equipe(alunos, projeto)
#       self.equipes.append(nova_equipe)
#        print('Equipe criada com sucesso!')
#a1 = Aluno('yonara', 1)
#a2 = Aluno('poly', 2)
#gerenciador = Gerenciador()
#gerenciador.Criar([a1,a2], 'projeto 1')
#gerenciador.Criar([a1], 'Projeto 1')

