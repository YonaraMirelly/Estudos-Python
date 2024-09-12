N,C,S = [int(x) for x in input().split()] 
comandos = list(map(int, input().split()))
coordenadas = [0 for i in range(N)] 
coordenadas[0] = 1 

valores = 0 
for i in comandos:
  if i== 1:
    valores += 1
    coordenadas[valores] += 1
  elif i == -1:
    valores -= 1
    coordenadas[valores] += 1

print(coordenadas[S-1])