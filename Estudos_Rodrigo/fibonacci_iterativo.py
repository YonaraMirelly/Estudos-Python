
# def fib(n, dic = {}):
#     if n in dic:
#         return dic[n]
#     if n <=2:
#         return 1
#     else:
#         dic[n] = fib(n-1, dic) + fib(n-2, dic)
#         return dic[n]
    
# print(fib(40))

def fib(n):
    if n < 1:
        return 0
    a, b, r = 0, 1, 1
    for _ in range(2, n):
        a,b = b,r
        r = a+b
    return r

print(fib(30))

