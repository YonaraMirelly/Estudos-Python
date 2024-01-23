print('-'*30)
def fatorial(num, show = False):
    f = 1
    for _ in range(num, 0 ,-1):
        if show:
            print(_, end='')
            if _ > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')

        f *= _
    return f
print(fatorial(5, show = True))
input()