x = int(input())
n = int(input())

total_usado = 0
for _ in range(n):
    mb = int(input())
    total_usado +=mb

restante = x* (n+1) - total_usado

if restante < 0:
    restante = 0

print(restante)