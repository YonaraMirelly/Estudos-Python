import matplotlib.pyplot as plt

# Dados fornecidos
# Algoritmo Genético
tempos_genetico = [0.03200793266296387, 0.1548924922943115, 0.4328819990158081, 1.3977570056915283, 
                   4.124902606010437, 8.169166254997254, 13.778930926322937, 27.47024550437927, 
                   83.48109023571014]
distancias_genetico = [25746, 21033, 17214, 13093, 11855, 11275, 10784, 9912, 9880]

# Algoritmo Memético
tempos_memetico = [0.04870371023813883, 0.1602171262105306, 0.3964198589324951, 0.6372496763865153, 
                   1.235387659072876, 3.622816777229309, 7.17328208287557, 11.988495834668477, 
                   28.392927466417947, 41.632505616526236, 70.869585507136332]
distancias_memetico = [8764, 8439, 8407, 8342, 8337, 8324, 8281, 8169, 8115, 7960, 7881]

# Algoritmo Vizinho Mais Próximo
tempos_vizinho = [0.002380172411600748, 0.003786945343017578, 0.002812353769938151, 
                  0.002304514249165853, 0.002232233683268229]
distancias_vizinho = [9358.729073024897, 9480.497552632258, 9366.29022555517, 
                      9367.582890961208, 9441.172270628806]

# Criar o gráfico
plt.figure(figsize=(10, 6))

# Plotar cada linha representando um algoritmo
plt.plot(distancias_genetico, tempos_genetico, marker='o', label='Genético')
plt.plot(distancias_memetico, tempos_memetico, marker='o', label='Memético')
plt.plot(distancias_vizinho, tempos_vizinho, marker='o', label='Vizinho Mais Próximo')

# Título e legendas
plt.title('Comparação de Algoritmos: Tempo vs Distância')
plt.xlabel('Distância')
plt.ylabel('Tempo (s)')
plt.legend()

# Exibir o gráfico
plt.grid(True)
plt.show()
