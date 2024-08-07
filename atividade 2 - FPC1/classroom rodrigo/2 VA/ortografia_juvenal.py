
def compararPalavras(palavraA, palavraB):
    A, B = len(palavraA), len(palavraB)
    dic = [[0] * 6 for i in range(22)]

    for i in range(3):
        dic[0][i + 2] = i

    for i in range(1, A + 1):
        for j in range(-2, 3):
            if i + j < 0 or i + j > B:
                continue
            if i + j == 0:
                dic[i][j + 2] = i
                continue
            if palavraA[i - 1] == palavraB[i + j - 1]:
                dic[i][j + 2] = dic[i - 1][j + 2]
            else:
                dic[i][j + 2] = dic[i - 1][j + 2] + 1
                if j != 2:
                    dic[i][j + 2] = min(dic[i][j + 2], dic[i - 1][j + 3] + 1)
                if j != -2:
                    dic[i][j + 2] = min(dic[i][j + 2], dic[i][j + 1] + 1)

    m = 10
    for i in range(-2, 3):
        if A + i < 0 or A + i > B:
            continue
        m = min(m, dic[A][i + 2] + B - A - i)
    return m < 3

N, M = map(int, input().split())
palavraCertas = [input() for i in range(N)]
palavraErradas = [input() for i in range(M)]

for palavraDigitada in palavraErradas:
    for palavraDicionario in palavraCertas:
        if compararPalavras(palavraDicionario, palavraDigitada):
            print(palavraDicionario, end=" ")
    print()