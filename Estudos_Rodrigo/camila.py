a = int(input())
b = int(input())
c = int(input())
if 5 <= a and b and c <= 100:
    if (a<=b) and (a>=c) or (a>=b) and (a<=c):
        print(a)
    elif (b>=a) and (b<=c) or (b<=a) and (b>=c):
        print(b)
    elif (c>=a) and (c<=b) or (c<=a) and (c>=b):
        print(c)
    else:
        print(a)
else:
    print('Digite os números corretamente!')