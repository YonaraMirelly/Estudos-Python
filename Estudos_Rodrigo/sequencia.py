n = int(input())
c = circulado_Atual = 0
for x in range(n):
    elemento = int(input())
    if elemento != circulado_Atual:
        circulado_Atual = elemento
        c+=1
print(c)

