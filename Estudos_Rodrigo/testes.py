m = {}
for i in range(3):
    for j in range(3):
        m[i,j] = [0]
    

for i in range(3):
    for j in range(3):
        print(f'[{m[i,j]}]', end = ' ')
    print()