def main(x, y):
    if y == 0:
        return 1
    else:
        return x * main(x, y-1)

if __name__ == "__main__":
    x, y = [float(i) for i in input().split()]
    result = main(x, y)
    print(f"{result:.4f}")
