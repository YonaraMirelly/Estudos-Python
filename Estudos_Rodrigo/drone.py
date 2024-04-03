a = int(input()) #altura
b = int(input()) #largura
c = int(input()) #profundidade

h = int(input())
l = int(input())

if 1 <= a and b and c and h and l <=100:
    if (a <= h and b <= l) or (a <= l and b <= h) or (a <= h and c <= l) or (a <= l and c <= h) or (b <= h and c <= l) or (b <= l and c <= h):
        print('S')
    else:
        print('N')
else:
    print('Digite números entre 1 e 100!')