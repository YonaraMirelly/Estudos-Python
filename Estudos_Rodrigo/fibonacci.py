
# def fib(n, dic = {}):
#     if n in dic:
#         return dic[n]
#     if n <=2:
#         return 1
#     else:
#         dic[n] = fib(n-1, dic) + fib(n-2, dic)
#         return dic[n]
    
# print(fib(40))
import time
def fib_esperto(n):
    if n <1:
        return 0
    a, b, r = 0, 1, 1
    for _ in range(2, n):
        a,b = b,r
        r = a+b
    return r

def nara(n, dic = {}):
    if n in dic:
        return dic[n]
    elif n <=2:
        return 1
    else:
        dic[n] = nara(n-1, dic)+nara(n-2, dic)
        return dic[n]
inicio = time.time()    
tic = time.process_time()
f = fib_esperto(100)
toc = time.process_time()
print(f'O de fib_esperto durou {tic-toc}')

tic = time.process_time()
nara = nara(100)
toc = time.process_time()
print(f'O de nara durou {tic-toc}')

final = time.time()

print(inicio)
print(final)