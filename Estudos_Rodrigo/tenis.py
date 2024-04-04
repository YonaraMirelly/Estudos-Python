venceu = 0
for _ in range(6):
    jogo = str(input())
    if jogo == "V":
        venceu+=1
if venceu>=5:
    print(1)
elif 3<=venceu<5:
    print(2)
elif 1<=venceu<3:
    print(3)
elif venceu<1:
    print(-1) 