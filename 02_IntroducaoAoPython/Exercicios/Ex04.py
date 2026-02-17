"""
By: Juliano Moreira Aleixo
https://julianoaleixo.dev
"""

distance = int(input("Digite a distância percorrida em Km: "))
if distance <= 200:
    price = distance * 0.5
else:
    price = distance * 0.45

print(f"O preço da viagem é de R${price:.2f}")
