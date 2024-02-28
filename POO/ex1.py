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

#class Produto:
#    qtde = 0
#    def __init__(self, codigo, preço):
#        self.__codigo = codigo
#        self.__preço = preço
#        Produto.qtde+=1
#    def Get(self):
#        return self.__preço
#    def Set(self, valor):
#        novo = self.__preço + valor
#        return novo
#a = Produto('1', 10)
#b = Produto('2', 20)
#print(f'preço a - {a.Get()}')
#print(f'preço de b - {b.Get()}')
#print(f'novo de A - {a.Set(50)}')
#print(f'quantidade - {Produto.qtde}')

#class Ponto:
#    def __init__(self, nome, a, b):
#        self.nome = nome
#        self.a = a
#        self.b = b
#    def __str__(self):
#        return f'{self.a} - {self.b}'
#p1 = Ponto('A', 100, 200)
#p2 = Ponto('B', 130, 150)
#p3 = Ponto('C', 500, 239)
#p4 = Ponto('outro', 199, 54)
#lista = [p1, p2, p3, p4]
#for elemento in lista:
#    print(elemento)

#class Biblioteca:
#    def __init__(self, titulo, autor):
#        self.titulo = titulo
#        self.autor = autor
#    def Alugar(self):
#        if self.alugado:
#            print('já alugado')
#        else:
#            self.alugado = True
#            print('livro foi alugado')
#    def Devolver(self):
#        if self.alugado:
#            self.alugado = False
#            print('livro foi devolvido')
#        else:
#            print('livro não está alugado!')
#class Livro:
#    def __init__(self):
#        self.livros_disponiveis = []
#        self.livros_alugados = []
#    def Adicionar_livro(self, livro):
#        self.livros_disponiveis(livro)
#    def Alugar_livro(self, titulo):
#        for livro in self.livros_disponiveis:
#            if livro.titulo == titulo:
#                livro.alugar
#                self.livros_disponiveis.remove(livro)
#                self.livros_alugados.append(livro)
#                return
#        print('livro não disponível no momento')
#    def Devolver(self, titulo):
#        for livro in self.livros_alugados:
#            if livro.titulo == titulo:
#                livro.Devolver()
#                self.livros_alugados.remove(livro)
#                self.livros_disponiveis.append(livro)
#                return
#    def Livro_mais_alugado(self):
#        if not self.livros_alugados:
#            return None
#        return max(self.livros_alugados, key=lambda livro:self.livros_alugados.count(livro)).titulo


#class Ingresso:
#    def __init__(self, valor):
#        self.valor = valor
#    def Imprime(self):
#        return self.valor
#class VIP(Ingresso):
#    def __init__(self, valor, adicional):
#        super().__init__(valor)
#        self.adicional = adicional
#    def Aumento(self):
#        novo = self.valor + self.adicional
#        return novo
#v1 = VIP(100, 50)
#print(f'Seu ingresso normal vale {v1.Imprime()} e o vip vale {v1.Aumento()}')


#class Forma:
#    def __init__(self):
#        self.area = 0
#        self.perimetro = 0
#class Retangulo(Forma):
#    def __init__(self, a, b):
#        super().__init__()
#        self.a = a
#        self.b = b
#    def CalculaArea(self):
#        self.area = self.a * self.b
#        return self.area
#    def CalcuraPerimetro(self):
#        self.perimetro = (2*self.a) + (2*self.b)
#        return self.perimetro
#class Triangulo(Forma):
#    def __init__(self, base, altura, c):
#        super().__init__()
#        self.base = base
#        self.altura = altura
#        self.c = c
#    def CalculaArea(self):
#        self.area = self.base * self.altura / 2
#        return self.area
#    def CalculaPerimetro(self):
#        self.perimetro = self.base +self.altura + self.c
#        return self.perimetro

#retangulo = Retangulo(2,4)
#triangulo = Triangulo(4,5,1)
#print(f'area do retangulo - {retangulo.CalculaArea()}')
#print(f'perimetro do retangulo - {retangulo.CalcuraPerimetro()}')
#print(f'area do triangulo - {triangulo.CalculaArea()}')
#print(f'perimetro do triangulo - {triangulo.CalculaPerimetro()}')

#class Atleta:
#    def __init__(self, nome, idade):
#        self.nome = nome
#        self.idade = idade
#    def Aposentar(self):
#        if self.idade>60:
#            print('aposentar')
#        else:
#            print('não aposentar')
#    def Aquecer(self):
#        return f'{self.nome} aquecendo...'
#class Corredor(Atleta):
#    def correr(self):
#        return f'{self.nome} correndo...'
#class Nadador(Atleta):
#    def nadar(self):
#        return f'{self.nome} nadando...'
#class Ciclista(Atleta):
#    def pedalar(self):
#        return f'{self.nome} pedalandi...'3
#class TRI(Corredor, Nadador, Ciclista):
#    pass
#tri = TRI('joao', 25)
#print(tri.Aposentar())
#print(tri.Aquecer())
#print(tri.correr())
#print(tri.nadar())

#class Conta:
#    def __init__(self, saldo):
#        self.saldo = saldo
#    def depositar(self, valor):
#        novo = self.saldo + valor
#        return novo
#    def saque(self, valor):
#        if self.saldo>valor:
#            self.saldo-=valor
#        else:
#            print('saldo insuficiente!')
#    def exibir(self):
#        print(f'saldo de R${self.saldo}')
#class ContaCorrente(Conta):
#    def __init__(self, saldo, taxa):
#        super().__init__(saldo)
#        self.taxa = taxa
#    def desconto(self):
#        self.saldo-=self.taxa
#class Poupança(Conta):
#    def __init__(self, saldo, rendimento):
#        super().__init__(self, saldo)
#        self.rendimento = rendimento
#    def Rendiment(self):
#        self.saldo * (1+self.rendimento/100)
#class ContaImposto(Conta):
#    def __init__(self, saldo, imposto):
#        super().__init__(saldo)
#        self.imposto = imposto
#    def CalculaImposto(self):
#        imposto = self.saldo *(self.imposto/100)
#        return imposto

