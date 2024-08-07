def misteriosa(n, s):
    if len(s) == n:
        print(s)
        return
    
    for i in ('0', '1'):
        a = s + i
        misteriosa(n, a)
        
    return ''
print('a forma do papel ->')
print(misteriosa(5, ''))

print('altenartivo -> ')
def gerar_combinacoes_binarias(n):
    # Inicializa a lista com uma string vazia
    combinacoes = ['']
    
    # Itera para gerar combinações de comprimento 1 até n
    for _ in range(n):
        novas_combinacoes = []
        for combinacao in combinacoes:
            novas_combinacoes.append(combinacao + '0')
            novas_combinacoes.append(combinacao + '1')
        combinacoes = novas_combinacoes
    
    # Imprime todas as combinações
    for combinacao in combinacoes:
        print(combinacao)

# Testa a função
gerar_combinacoes_binarias(5)
