a = int(input())
b = int(input())
c = int(input())
if 0<= a and b and c <= 500:
    if (b-a) < (c-b):
        print(1)
    elif (b-a) > (c-b):
        print(-1)
    elif (b-a) == (c-b):
        print(0)
else:
    print('Tente novamente!')