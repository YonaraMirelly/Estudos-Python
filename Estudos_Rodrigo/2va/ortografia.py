
def comparar(palavra_1, palavra_2):
    A, B = len(palavra_1), len(palavra_2)
    dicionario = [[0] * 6 for i in range(22)]

    for i in range(3):
        dicionario[0][i + 2] = i

    for i in range(1, A + 1):
        for j in range(-2, 3):
            if i + j < 0 or i + j > B:
                continue
            if i + j == 0:
                dicionario[i][j + 2] = i
                continue
            if palavra_1[i - 1] == palavra_2[i + j - 1]:
                dicionario[i][j + 2] = dicionario[i - 1][j + 2]
            else:
                dicionario[i][j + 2] = dicionario[i - 1][j + 2] + 1
                if j != 2:
                    dicionario[i][j + 2] = min(dicionario[i][j + 2], dicionario[i - 1][j + 3] + 1)
                if j != -2:
                    dicionario[i][j + 2] = min(dicionario[i][j + 2], dicionario[i][j + 1] + 1)
    m = 10
    for i in range(-2, 3):
        if A + i < 0 or A + i > B:
            continue
        m = min(m, dicionario[A][i + 2] + B - A - i)
    return m < 3

N, M = map(int, input().split())
palavras_corretas = [input() for i in range(N)]
palavras_erradas = [input() for i in range(M)]

for palavraDigitada in palavras_erradas:
    for palavraDicionario in palavras_corretas:
        if comparar(palavraDicionario, palavraDigitada):
            print(palavraDicionario, end=" ")
    print()