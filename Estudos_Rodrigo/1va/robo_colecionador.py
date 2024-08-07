# ok
def rali_dos_robos():
    #loop infinito
    while True:
        N, M, S = map(int, input().split()) # dividir em três partes e converter para inteiro
        if N == 0 and M == 0 and S == 0: # fim da entrada (como se fosse o caso base)
            break
        arena = []
        for _ in range(N):
            arena.append([char for char in input().strip()]) #lista de caracteres (list comprehension)
        instrucoes = input().strip() # sequência de instruções para o robô
        # Direções: N=0, L=1, S=2, O=3
        mapa_direcoes = {'N': 0, 'L': 1, 'S': 2, 'O': 3} # mapeiar as direções para os índices de 0 a 3
        movimentos_direcao = [(0, -1), (1, 0), (0, 1), (-1, 0)] # listar as mudanças de posição #esquerda - direita - cima - baixo
        direcao_atual = 0 # indica norte
        posicao_atual = (0, 0) # será atualizada
        # encontrando posição e direção iniciais
        for i in range(N):
            for j in range(M):
                if arena[i][j] in mapa_direcoes:
                    posicao_atual = (i, j)
                    direcao_atual = mapa_direcoes[arena[i][j]]
                    arena[i][j] = '.' # substitui para indicar que não há mais direção inicial
                    break
        figurinhas_coletadas = 0 # contar quantas figurinhas o robô coletou
        for instrucao in instrucoes:
            if instrucao == 'D':
                direcao_atual = (direcao_atual + 1) % 4 # 90 graus para direita
            elif instrucao == 'E':
                direcao_atual = (direcao_atual - 1) % 4 # 90 graus para a esquerda
            elif instrucao == 'F':
                di, dj = movimentos_direcao[direcao_atual]
                ni, nj = posicao_atual[0] + dj, posicao_atual[1] + di
                if 0 <= ni < N and 0 <= nj < M and arena[ni][nj] != '#': # verificar se a nova posição está dentro dos limites
                    posicao_atual = (ni, nj) # atualizar posição atual
                    if arena[ni][nj] == '*':
                        figurinhas_coletadas += 1 # acrescenta na variável
                        arena[ni][nj] = '.' # remover a figurinha da arena
        print(figurinhas_coletadas)
# chamar a função
rali_dos_robos()
