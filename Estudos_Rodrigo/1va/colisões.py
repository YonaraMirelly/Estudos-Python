r1 = [int(i) for i in input().split()]
r2 = [int(i) for i in input().split()]
if r1[-1] and r1[-2] > r2[0] and r2[1] or r1 == r2:
    print(1)
elif r2[-1] and r2[-2] > r1[0] and r1[1]:
    print(1)
else:
    print(0)
