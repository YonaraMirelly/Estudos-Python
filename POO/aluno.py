class Aluno:
    def __init__(self, nome, curso, tempoSemDormir):
        self.nome = nome
        self.curso = curso
        self.tempoSemDormir = tempoSemDormir

    def estudar(self, horas):
        self.tempoSemDormir += horas
    
    def dormir(self, horasSono):
        self.tempoSemDormir -= horasSono
    
aluno = Aluno('yonara', 'SI', 8)
print(f'Tempo sem dormir-> {aluno.tempoSemDormir}')
aluno.estudar(8)
print(f'Tempo sem dormir após estudar-> {aluno.tempoSemDormir}')
aluno.dormir(6)
print(f'Tempo sem dormir após dormir-> {aluno.tempoSemDormir}')
