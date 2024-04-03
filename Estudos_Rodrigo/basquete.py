d = int(input())
if 1 <= d <= 2000:
    if d <= 800:
        print(1)
    elif 800 < d <= 1400:
        print(2)
    elif 1400 < d <= 2000:
        print(3)
else:
    print('Digite valores entre 1 e 2000!')