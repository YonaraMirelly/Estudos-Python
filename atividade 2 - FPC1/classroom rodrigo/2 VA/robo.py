
class Robo:
    def __init__(self, arena, posição_inicial, direção_inicial):
        self.arena = arena
        self.posição = posição_inicial
        self.direção = direção_inicial
        self.figurines_coletados = 0
    
    def mover(self, instrução):
        if instrução == 'D':
            if self.direção == 'N':
                self.direção = 'L'
            elif self.direção == 'S':
                self.direção = 'O'
            elif self.direção == 'L':
                self.direção = 'S'
            elif self.direção == 'O':
                self.direção = 'N'
        elif instrução == 'E':
            if self.direção == 'N':
                self.direção = 'O'
            elif self.direção == 'S':
                self.direção = 'L'
            elif self.direção == 'L':
                self.direção = 'N'
            elif self.direção == 'O':
                self.direção = 'S'
        elif instrução == 'F':
            próxima_posição = self.obter_próxima_posição()
            if self.movimento_valido(próxima_posição):
                self.posição = próxima_posição
                if self.arena[self.posição[0]][self.posição[1]] == '*':
                    self.figurines_coletados += 1
    
    def obter_próxima_posição(self):
        if self.direção == 'N':
            return (self.posição[0] - 1, self.posição[1])
        elif self.direção == 'S':
            return (self.posição[0] + 1, self.posição[1])
        elif self.direção == 'L':
            return (self.posição[0], self.posição[1] + 1)
        elif self.direção == 'O':
            return (self.posição[0], self.posição[1] - 1)
    
    def movimento_valido(self, próxima_posição):
        n, m = len(self.arena), len(self.arena[0])
        if próxima_posição[0] < 0 or próxima_posição[0] >= n or próxima_posição[1] < 0 or próxima_posição[1] >= m:
            return False
        if self.arena[próxima_posição[0]][próxima_posição[1]] == '#':
            return False
        return True

def coletar_figurines():
    while True:
        n, m, s = map(int, input().split())
        if n == 0 and m == 0 and s == 0:
            break
        arena = []
        posição_inicial = None
        direção_inicial = None
        for i in range(n):
            linha = input()
            arena.append(linha)
            if 'N' in linha:
                posição_inicial = (i, linha.index('N'))
                direção_inicial = 'N'
            elif 'S' in linha:
                posição_inicial = (i, linha.index('S'))
                direção_inicial = 'S'
            elif 'L' in linha:
                posição_inicial = (i, linha.index('L'))
                direção_inicial = 'L'
            elif 'O' in linha:
                posição_inicial = (i, linha.index('O'))
                direção_inicial = 'O'

        instruções = input()
        robo = Robo(arena, posição_inicial, direção_inicial)
        for instrução in list(instruções):  # Convertendo para lista de caracteres
            robo.mover(instrução)
        print(robo.figurines_coletados)


coletar_figurines()
