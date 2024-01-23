times = ('Palmeiras', 
         'Flamengo', 'Atlético Mineiro', 'Fortaleza', 'Bragantino', 'Athletico' 
         'Paranaense', 'Fluminense', 'Ceará', 'Internacional', 'Santos', 'Juventude', 'Bahia', 'Corinthians', 
         'América Mineiro', 'São Paulo', 'Cuiabá', 'Grêmio', 'Sport', 'Chapecoense', 'Atlético Goianiense')
print('='*30)
print(f'\033[1;32mLISTA DE TIMES DO BRASILEIRÃO:\033[m {times}')
print('='*30)
print(f'\033[1;33mOs cinco primeiros times são:\033[m {times[:5]}')
print('='*30)
print(f'\033[1;34mOs quatro últimos são:\033[m {times[16:]}')
print('='*30)
print(f'\033[1;36mtimes em ordem alfabética:\033[m {sorted(times)}')
print('='*30)
print(f'\033[1;35mO Chapecoense está na {times.index("Chapecoense")+1}ª posição.\033[m')