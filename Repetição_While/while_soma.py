n = soma = cont = 0
while True:
    n = int(input('Digite um valor \033[1;31m[999 para parar]\033[m: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Você digitou {cont} valores e a soma deles é {soma}!')
input()