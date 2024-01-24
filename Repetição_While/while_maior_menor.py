n = cont = media = soma = menor = maior= 0
escolha = 'S'
while escolha in 'Ss':
   n = int(input('Digite um número: '))
   soma +=n
   cont +=1
   if cont == 1:
      menor = maior = n
   else:
      if n > maior:
         maior = n
      if n < menor:
         menor = n
   escolha = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / cont
print('Você digitou {} valores e a média entre eles é {:.2f}.'.format(cont, media))
print('O maior valor é {} e o menor valor é {}.'.format(maior,menor))
input()