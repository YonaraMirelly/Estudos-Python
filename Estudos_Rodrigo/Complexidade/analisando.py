def main():
    lista = [float(i) for i in input().split()]
    print(lista)
    if lista[0] > lista[1]:
        print('Pedro')
    else:
        print('Paulo')

if __name__ == "__main__":
    main()
