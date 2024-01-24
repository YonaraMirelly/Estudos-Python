extenso  = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = 0
opçao = 'SN'
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    print('Tente novamente.', end=' ')
print(f'Você digitou o número {extenso[n]}')
while True:
  resp = str(input('Deseja continuar?[S/N]: ')).upper().strip()
  if resp != 'S' and resp != 'N':
      print('Comando inválido. Digite S para SIM e N para NÃO')
  if resp == 'N':
    break
  if resp == 'S':
    while True:
      num = int(input('Digite um número entre 0 e 20: '))
      if 0 <= num <= 20:
        break
      print('Tente novamente.', end=' ')
    print(f'Você digitou o número {extenso[num]}')
print('Fim do programa')
input()