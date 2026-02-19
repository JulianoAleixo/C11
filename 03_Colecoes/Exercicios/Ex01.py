"""
By: Juliano Moreira Aleixo
https://julianoaleixo.dev
"""

teams = ["Corinthians", "São Paulo", "Santos", "Palmeiras", "Bragantino"]

print("3 primeiros colocados: ")
print(teams[:3])

print()
print("2 últimos colocados: ")
print(teams[-2:])

print()
print("Times em ordem alfabética")
teams_sorted = sorted(teams)
print(teams_sorted)

print()
print("Posição da tabela que se encontra o Barcelona")
if "Barcelona" in teams:
    print(teams.index("Barcelona"))
else:
    print("Nenhum Barcelona encontrado")
