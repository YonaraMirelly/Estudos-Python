N = int(input())
alturas = [int(i) for i in input().split()]
print(alturas)
if len(alturas)<3 or len(alturas)%2!=0:
    print("N")
else:
    valor = alturas[0] + alturas[-1]
    for i in range(N//2):
        if alturas[i] + alturas[-(i+1)] != valor:
            print('N')
            break
    else:
        print('S')