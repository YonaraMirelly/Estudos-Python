def main():
    lista = [int(i) for i in input().split()]
    num = int(input())
    if num in lista:
        print('SIM')
    else:
        print('NÃO')
    return ''
if __name__ == "__main__":
    print(main())
