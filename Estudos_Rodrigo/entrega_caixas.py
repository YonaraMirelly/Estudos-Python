a = int(input())
b = int(input())
c = int(input())
if 1 <= a and b and c <=1000:
    if (a<b and a<c and b==c) or (b<a and b<c and a==c) or (c>a and c>b and a==b and (a+b)>c):
        print(2)
    elif (a+b)<c or (b+c)<a or (a+c)<b:
        print(1)
    else:
        print(3)
else:
    print('Digite os números corretamente.')