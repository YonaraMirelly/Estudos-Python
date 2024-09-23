def fat(n):
    if n<0:
        return 0
    if n ==0:
        return 
    if n == 1:
        return 1
    else:
        return n * fat(n-1)
    
n = int(input('digite um número: '))
print(fat(n))