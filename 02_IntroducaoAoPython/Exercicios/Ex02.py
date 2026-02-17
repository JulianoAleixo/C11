"""
By: Juliano Moreira Aleixo
https://julianoaleixo.dev
"""

number = int(input("Escolha um número para o cálculo da tabuada: "))
min = int(input("Escolha o valor mínimo do intervalo: "))
max = int(input("Escolha o valor máximo do intervalo: "))

for i in range(min, max + 1):
    print(f"{number} * {i} = {number * i}")
