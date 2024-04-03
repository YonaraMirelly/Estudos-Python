

c1 = int(input('comprimento 1: '))
l1 = int(input('largura 1: '))
c2 = int(input('comprimento 2: '))
l2 = int(input('largura 2: '))
if not 1 < c1 or l1 or c2 or l2 < 100:
    print('Digite números entre 1 e 100!')
else:
    area1 = c1 * l1
    aerea2 = c2 * l2
    if area1 > aerea2:
        print(area1)
    else:
        print(aerea2)