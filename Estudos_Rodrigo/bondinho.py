a = int(input())
b = int(input())
if 1 <= a and b <= 50:
    if a + b > 50:
        print('N')
    else:
        print('S')
else:
    print('Digite números entre 1 e 50!')