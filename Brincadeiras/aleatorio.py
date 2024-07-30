def classificar_pacientes(pacientes):
    # Ordem de prioridade dos planos
    prioridade_planos = {
        "premium": 1,
        "diamante": 2,
        "ouro": 3,
        "prata": 4,
        "bronze": 5,
        "resto": 6
    }
    
    # Função para comparar dois pacientes
    def compara(paciente1, paciente2):
        nome1, plano1, gravidade1 = paciente1
        nome2, plano2, gravidade2 = paciente2
        
        # Comparar pelo plano de pagamento
        if prioridade_planos[plano1] != prioridade_planos[plano2]:
            return prioridade_planos[plano1] < prioridade_planos[plano2]
        
        # Comparar pela gravidade
        if gravidade1 != gravidade2:
            return gravidade1 > gravidade2
        
        # Comparar pelo nome
        return nome1 < nome2
    
    # Implementação da ordenação por inserção
    for i in range(1, len(pacientes)):
        chave = pacientes[i]
        j = i - 1
        while j >= 0 and not compara(pacientes[j], chave):
            pacientes[j + 1] = pacientes[j]
            j -= 1
        pacientes[j + 1] = chave
    
    # Retornar a lista ordenada de pacientes
    return pacientes

# Ler a entrada
n = int(input().strip())
pacientes = []

for _ in range(n):
    entrada = input().strip().split()
    nome = entrada[0]
    plano = entrada[1]
    gravidade = int(entrada[2])
    pacientes.append((nome, plano, gravidade))

# Obter a classificação final dos pacientes
classificados = classificar_pacientes(pacientes)

# Imprimir a fila de atendimento
for paciente in classificados:
    print(paciente[0])
