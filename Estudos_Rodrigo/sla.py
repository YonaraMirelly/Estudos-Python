

def fib(n, dic = {}):
    if n in dic:
        return dic[n]
    elif n <=2:
        return 1
    else:
        dic[n] = fib(n-1, dic)+fib(n-2, dic)
        return dic[n]

print(fib(50))