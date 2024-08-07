#ok
def main():
    n = int(input()) # número de degraus
    pilha = [] # vetor de degraus
    soma = 0 # soma da pa
    moves = 0 # movimentos totais
    movimentos = 0 # movimento espefícifo quando um elemento é maior que seu índice ajustado
# adicionando tudo no vetor pilha e somando os elementos descritos
    for _ in range(n):
        valor = int(input()) #qtde de cubos em cada uma das pilhas
        pilha += [valor]
        soma += valor
    b = (((2*soma)// n) + (n-1)) // 2 # definir uma distribuição média ajustada dos elementos da pilha
    a = 1 + b - n # a é usado como ajuste para os índices dos elementos da pilha
    for i in range(n): # intera por cada índice da pilha
        moves += (pilha[i] - (i+a))
        if pilha[i] > i+a: # verifica se o elemento da pilha é maior do que o seu índice ajustado
            movimentos += (pilha[i] - (i+a))
    if moves != 0: # pilha não pode ser ajustada corretamente
        print('-1')
    else:
        print(movimentos) # indica os movimentos mínimos para ajustar a pilha.
if __name__ == "__main__":
    main()