m = int(input())
a = int(input())
b = int(input())
if (40 <= m <= 110) and (1<= a<=m) and (1<= b<=m) and (a!=b):
    c = m - (a+b)
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    elif c > a and c > b:
        print(c)
else:
    print('Tente novamente!')