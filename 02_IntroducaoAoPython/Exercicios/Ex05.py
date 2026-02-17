"""
By: Juliano Moreira Aleixo
https://julianoaleixo.dev
"""

number = ""
while 1:
    number = input("Entre um número entre 1000 e 9999: ")
    if 1000 <= int(number) <= 9999:
        break

print(f"Unidade: {number[3]}")
print(f"Dezena: {number[2]}")
print(f"Centena: {number[1]}")
print(f"Milhar: {number[0]}")
