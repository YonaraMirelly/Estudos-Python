# doces_disponiveis = int(input())
# x = int(input())
# y = int(input())
# z = int(input())

# quantidade = 0
# lista = [x, y, z]
# if x > y:
#         lista[0], lista[1] = lista[1], lista[0]
# if y < z:
#         lista[1], lista[2] = lista[2], lista[1]
# if y > z:
#         lista[1], lista[2] = lista[2], lista[1]

# doces_disponiveis -= lista[0]
# quantidade +=1
# if doces_disponiveis >= lista[1]:
#     doces_disponiveis -= lista[1]
#     quantidade +=1
#     if doces_disponiveis >= lista[2]:
#         doces_disponiveis -= lista[2]
#         quantidade +=1
#         print(quantidade)
#     else:
#         print(quantidade)
# else:
#     print(quantidade)

def max_pokemons_evolved(N, X, Y, Z):
    candies_needed = [X, Y, Z]
    candies_needed.sort()

    evolved_count = 0
    for candies in candies_needed:
        if N >= candies:
            N -= candies
            evolved_count += 1
        else:
            break
    
    return evolved_count

# Leitura dos dados de entrada
N = int(input())  # Número de doces disponíveis
X = int(input())  # Doces necessários para a primeira pô-que-mão evoluir
Y = int(input())  # Doces necessários para a segunda pô-que-mão evoluir
Z = int(input())  # Doces necessários para a terceira pô-que-mão evoluir

# Chamada da função e impressão do resultado
print(max_pokemons_evolved(N, X, Y, Z))


    