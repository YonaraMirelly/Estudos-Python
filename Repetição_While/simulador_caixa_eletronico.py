print('='*30)
print('{:^30}'.format('BANCO SEVERINA'))
print('='*30)
n = int(input('Que valor você quer sacar? R$'))
totalced = 0
ced = 50   
total = n 
while True:
    if total >= ced:
        total-=ced
        totalced+=1
    else:
        if totalced >0:
            print(f'Total de {totalced} cédulas de R${ced}')
        if ced ==50:
            ced = 20
        elif ced ==20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total ==0:
            break
print('='*30)
print('Volte sempre ao Banco Severina! :)')
input()

   
   
