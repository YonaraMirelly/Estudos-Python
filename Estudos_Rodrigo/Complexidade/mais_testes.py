def max_valor_cano_recursivo(T, comprimentos_valores, memo):
    if T == 0:
        return 0
    if T in memo:
        return memo[T]
    
    max_valor = 0
    for comprimento, valor in comprimentos_valores:
        if comprimento <= T:
            valor_atual = valor + max_valor_cano_recursivo(T - comprimento, comprimentos_valores, memo)
            max_valor = max(max_valor, valor_atual)
    memo[T] = max_valor
    return max_valor

# Leitura da entrada
N, T = map(int, input().split())
comprimentos_valores = [tuple(map(int, input().split())) for _ in range(N)]

# Inicializa o dicionário de memoização
memo = {}
# Calcula e imprime o resultado
print(max_valor_cano_recursivo(T, comprimentos_valores, memo))
