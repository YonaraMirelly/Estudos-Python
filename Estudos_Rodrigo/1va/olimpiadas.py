# ok
def classificar_paises(n, m, modalidades):
    medalhas = {i: {'ouro': 0, 'prata': 0, 'bronze': 0} for i in range(1, n+1)}
    for modalidade in modalidades:
        ouro, prata, bronze = modalidade
        medalhas[ouro]['ouro'] += 1
        medalhas[prata]['prata'] += 1 
        medalhas[bronze]['bronze'] += 1 
    paises = [[i, medalhas[i]['ouro'], medalhas[i]['prata'], medalhas[i]['bronze']] for i in range(1,n+1)] 
    def compara(pais1, pais2):
        if pais1[1] != pais2[1]:
            return pais1[1] > pais2[1]
        if pais1[2] != pais2[2]:
            return pais1[2] > pais2[2]
        if pais1[3] != pais2[3]:
            return pais1[3] > pais2[3]
        return pais1[0] < pais2[0]
    for i in range(1, len(paises)):
        chave = paises[i]
        j = i-1
        while j>= 0 and not compara(paises[j], chave):
            paises[j+1] = paises[j]
            j-=1
        paises[j+1] = chave
    resultado = [pais[0] for pais in paises] 
    return resultado

n, m = map(int, input().split())
modalidades = [tuple(map(int, input().split())) for _ in range(m)]
classificação = classificar_paises(n, m, modalidades)
print(' '.join(map(str, classificação)))      