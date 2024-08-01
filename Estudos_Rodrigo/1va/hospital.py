# def classificação(pacientes):
#     prioridade_planos = {
#         'premium': 1,
#         'diamante': 2,
#         'ouro': 3,
#         'prata': 4,
#         'bronze': 5,
#         'resto': 6
#     }

# #função para comparar dois clientes ->
#     def compara(p1, p2):
#         nome1, plano1, gravidade1 = p1
#         nome2, plano2, gravidade2 = p2

#         #compara plano de pagamento
#         if prioridade_planos[plano1] != prioridade_planos[plano2]:
#             return prioridade_planos[plano1] < prioridade_planos[plano2]
#         #compara pela gravidade
#         if gravidade1 != gravidade2:
#             return gravidade1 > gravidade2
        
#         #compara pelo nome
#         return nome1 < nome2 
    
#     for i in range(1, len(pacientes)):
#         chave = pacientes[i]
#         j = i -1
#         while j >=0 and not compara(pacientes[j], chave):
#             pacientes[j+1] = pacientes[j]
#             j -=1
        
#         pacientes[j+1] = chave

#     return pacientes

# #entrada ->
# n = int(input().strip())
# pacientes = []

# for _ in range(n):
#     entrada = input().strip().split()
#     nome = entrada[0]
#     plano = entrada[1]
#     gravidade = int(entrada[2])
#     pacientes.append((nome, plano, gravidade))

# classificados = classificação(pacientes)

# for paciente in classificados:
#     print(paciente[0])

######resolução de rodrigo###### olimpiada e hospital eh mesmo código
from typing import Dict
dic_ordem = {'premium': 0, 'diamante': 1, 'ouro':2, 'prata':3, 'bronze':4, 'resto':5}
def comparação(paciente1: Dict[str, int, str], paciente2: Dict[str, int, str]):
    if dic_ordem[paciente1['plano']] > dic_ordem[paciente2['plano']]:
        return 1
    if paciente1['gravidade'] > paciente2['gravidade']:
        return 1
    if paciente1['nome'].lower() < paciente2['nome'].lower():
        return 1
    return -1

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if comparação(A[j], x) == 1:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]
    return i+1

#implementando no quick_sort()
def quicksort(A, p, r):
    if p <= r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

