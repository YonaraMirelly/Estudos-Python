
def testa(a, b):
    sa, sb = len(a), len(b)
    t = [[0] * 6 for _ in range(22)]

    for i in range(3):
        t[0][i + 2] = i

    for i in range(1, sa + 1):
        for j in range(-2, 3):
            if i + j < 0 or i + j > sb:
                continue
            if i + j == 0:
                t[i][j + 2] = i
                continue
            if a[i - 1] == b[i + j - 1]:
                t[i][j + 2] = t[i - 1][j + 2]
            else:
                t[i][j + 2] = t[i - 1][j + 2] + 1
                if j != 2:
                    t[i][j + 2] = min(t[i][j + 2], t[i - 1][j + 3] + 1)
                if j != -2:
                    t[i][j + 2] = min(t[i][j + 2], t[i][j + 1] + 1)

    m = 10
    for i in range(-2, 3):
        if sa + i < 0 or sa + i > sb:
            continue
        m = min(m, t[sa][i + 2] + sb - sa - i)

    return m < 3


n, m = map(int, input().split())

d = [input() for _ in range(n)]
p = [input() for _ in range(m)]

for palavra_texto in p:
    for palavra_dic in d:
        if testa(palavra_dic, palavra_texto):
            print(palavra_dic, end=" ")
    print()