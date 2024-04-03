p = int(input())
d1 = int(input())
d2 = int(input())
soma = d1+d2
if soma % 2 == 0:
    if p == 0:
        print(0) #alice ganha
    else:
        print(1) #bob ganha

else:
    if p == 0:
        print(1) # bob ganha
    else:
        print(0) # alice ganha
