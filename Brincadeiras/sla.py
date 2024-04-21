def main():
    a, b, c = [int(i) for i in input().split()]
    if a != b and a != c:
        print('A')
    elif b != a and b != c:
        print('B')
    elif c != a and c != b:
        print('C')
    else:
        print('*')
    return ''

if __name__ == "__main__":
    print(main())