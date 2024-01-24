cid = str(input('\033[1;35;42mEm que cidade você nasceu?\033[m ')).strip()
print('\033[1;35;43mSua cidade começa com a palavra Santo?\033[m')
print(cid[:5].upper() == 'SANTO')
input()



