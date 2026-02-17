"""
By: Juliano Moreira Aleixo
https://julianoaleixo.dev
"""

while 1:
    value = input("Digite seu sexo (M/F): ").upper()
    match value:
        case "M":
            print("Homem")
        case "F":
            print("Mulher")
        case _:
            continue
    break
