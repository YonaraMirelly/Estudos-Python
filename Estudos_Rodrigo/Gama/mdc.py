def mdc(a, b):
    if a == 0 or b == 0:
        return "indeterminado"
    if a == b:
        return a
    elif a > b:
        return mdc(a-b, b)
    return mdc(b, a%b)

a, b = [int(i) for i in input().split()]
print(mdc(a, b))
