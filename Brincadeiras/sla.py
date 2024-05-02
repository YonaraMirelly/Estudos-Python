def main():
    n = int(input())
    matriz = []
    for i in range(n):
        matriz += [[int(j) for j in input().split()]]

    max_peso = 0
    for i in range(n):
        linha_soma = 0
        for j in range(n):
            linha_soma += matriz[i][j]
        for j in range(n):
            coluna_soma = 0
            for k in range(n):
                coluna_soma += matriz[k][j]
            peso = linha_soma + coluna_soma - 2 * matriz[i][j]
            if peso > max_peso:
                max_peso = peso

    return max_peso    
            
if __name__ == "__main__":
    print(main())