def classificação(pacientes):
    prioridade_planos = {
        'premium': 1,
        'diamante': 2,
        'ouro': 3,
        'prata': 4,
        'bronze': 5,
        'resto': 6
    }

#função para comparar dois clientes ->
    def compara(p1, p2):
        nome1, plano1, gravidade1 = p1
        nome2, plano2, gravidade2 = p2

        #compara plano de pagamento
        if prioridade_planos[plano1] != prioridade_planos[plano2]:
            return prioridade_planos[plano1] < prioridade_planos[plano2]
        #compara pela gravidade
        if gravidade1 != gravidade2:
            return gravidade1 > gravidade2
        
        #compara pelo nome
        return nome1 < nome2 
    
    for i in range(1, len(pacientes)):
        chave = pacientes[i]
        j = i -1
        while j >=0 and not compara(pacientes[j], chave):
            pacientes[j+1] = pacientes[j]
            j -=1
        
        pacientes[j+1] = chave

    return pacientes

#entrada ->
n = int(input().strip())
pacientes = []

for _ in range(n):
    entrada = input().strip().split()
    nome = entrada[0]
    plano = entrada[1]
    gravidade = int(entrada[2])
    pacientes.append((nome, plano, gravidade))

classificados = classificação(pacientes)

for paciente in classificados:
    print(paciente[0])