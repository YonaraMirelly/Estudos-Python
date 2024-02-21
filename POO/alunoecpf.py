class Aluno:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Equipe:
    def __init__(self, projeto):
        self.participantes = []
        self.projeto = projeto

    def adicionarAluno(self, aluno):
        self.participantes.append(aluno)

class GerenciadorEquipes:
    def __init__(self):
        self.equipes = []

    def criarEquipe(self, alunos, projeto):
        equipe = Equipe(projeto)
        for aluno in alunos:
            if any(aluno.cpf == a.cpf for e in self.equipes for a in e.participantes):
                print(f"Aluno {aluno.nome} já está em outra equipe.")
                return
            if any(aluno.cpf == a.cpf for a in equipe.participantes):
                print(f"Aluno {aluno.nome} já está na equipe a ser criada.")
                return
        equipe.participantes.extend(alunos)
        self.equipes.append(equipe)
        print(f"Equipe para o projeto {projeto} criada com sucesso.")

# Testando as classes
aluno1 = Aluno("João", "123456789")
aluno2 = Aluno("Maria", "987654321")
aluno3 = Aluno("Pedro", "456789123")

gerenciador = GerenciadorEquipes()

gerenciador.criarEquipe([aluno1, aluno2], "Projeto A")  # Equipe 1
gerenciador.criarEquipe([aluno3], "Projeto B")  # Equipe 2
gerenciador.criarEquipe([aluno1, aluno3], "Projeto A")  # Equipe 3 (não pode ser criada porque aluno1 já está em outra equipe)
