posi = [int(i) for i in input().split()]
corre = posi[-1]

if posi[0] < posi[1] and posi[1] > posi[2] > posi[0] and corre == -1:
    print('S')
elif posi[2] > posi[0] and posi[2] > posi[1] and corre == 1:
    print('S')
elif posi[2] < posi[0] and posi[2] < posi[1] and corre == 1:
    print('S')
elif posi[0] > posi[1] and posi[1] > posi[2] < posi[0] and corre == -1:
    print('S')
else:
    print("N")