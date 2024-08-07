#ok
n = int(input()) #O(1)
pessoas = [int(i) for i in input().split()] #O(1)
n_retirados = int(input()) #O(1)
retirados = [int(i) for i in input().split()] #O(1)
for i in range(n_retirados): #O(n)
    if retirados[i] in pessoas: #O(n)
        pessoas = [a for a in pessoas if a != retirados[i]] #O(n)
print(pessoas) #O(1)