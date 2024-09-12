
def pode_cortar(N, K, bolos, tamanho_fatia):
    total_fatias = 0
    for bolo in bolos:
        total_fatias += bolo // tamanho_fatia  
    return total_fatias >= N  
def meu_maior(lista):
    maior = lista[0]  
    for elemento in lista:
        if elemento > maior:
            maior = elemento  
    return maior
def maior_tamanho_fatia(N, K, bolos):
    inicio = 1  
    fim = meu_maior(bolos)  
    resultado = 0
    while inicio <= fim:
        tamanho_fatia = (inicio + fim) // 2  
        if pode_cortar(N, K, bolos, tamanho_fatia):
            resultado = tamanho_fatia
            inicio = tamanho_fatia + 1  
        else:
            fim = tamanho_fatia - 1 

    return resultado
N = int(input())  
K = int(input())  
bolos = list(map(int, input().split()))  

print(maior_tamanho_fatia(N, K, bolos))
