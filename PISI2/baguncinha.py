import itertools

# Função para calcular o custo entre dois pontos
def calcular_custo(ponto1, ponto2):
    return abs(ponto1[0] - ponto2[0]) + abs(ponto1[1] - ponto2[1])

# Função para calcular o custo total de uma permutação de pontos
def calcular_custo_total(permutacao, pontos):
    custo_total = 0
    for i in range(len(permutacao) - 1):
        custo_total += calcular_custo(pontos[permutacao[i]], pontos[permutacao[i + 1]])
    return custo_total

# Função para ler a matriz do arquivo
def ler_matriz(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        linhas = file.readlines()
        num_linhas, num_colunas = map(int, linhas[0].split())
        matriz = [linha.split() for linha in linhas[1:]]
        pontos = {}
        for i in range(num_linhas):
            for j in range(num_colunas):
                if matriz[i][j] != '0' and matriz[i][j] != 'R':
                    pontos[matriz[i][j]] = (i, j)
        return pontos

# Função principal para encontrar a sequência de entrega de menor custo
def encontrar_menor_sequencia_entrega(nome_arquivo):
    pontos = ler_matriz(nome_arquivo)
    entregas = list(pontos.keys())
    menor_custo = float('inf')
    menor_sequencia = None
    for permutacao in itertools.permutations(entregas):
        custo = calcular_custo_total(permutacao, pontos)
        if custo < menor_custo:
            menor_custo = custo
            menor_sequencia = permutacao
    return ' '.join(menor_sequencia)

# Testando a função com o exemplo fornecido
print(encontrar_menor_sequencia_entrega('pp.txt'))
