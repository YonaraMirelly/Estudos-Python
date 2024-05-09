#### esse fica girando infinitamente
def combinacoes_sem_repeticao(nums, k, inicio=0, atual=[]):
    if len(atual) == k:
        yield tuple(atual)
    else:
        for i in range(inicio, len(nums)):
            atual.append(nums[i])
            yield from combinacoes_sem_repeticao(nums, k, i + 1, atual)
            atual.pop()

def gerar_jogos_mega_sena():
    numeros = list(range(1, 61))
    for jogo in combinacoes_sem_repeticao(numeros, 6):
        print(jogo)

# Chamar a função para gerar os jogos
gerar_jogos_mega_sena()





# import random

# def gerar_jogos_mega_sena(n_jogos):
#     for _ in range(n_jogos):
#         jogo = random.sample(range(1, 61), 6)
#         jogo.sort()
#         print(jogo)

# # Chamar a função para gerar os jogos
# gerar_jogos_mega_sena(10)  # Gerar 10 jogos aleatórios
