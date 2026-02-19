"""
By: Juliano Moreira Aleixo
https://julianoaleixo.dev
"""

people = []
for i in range(3):
    name = input('Nome: ')
    weight = int(input('Weight: '))
    people.append({"name": name, "weight": weight})
    print()


heaviest = people[0]
for i in range(3):
    if people[i]["weight"] > heaviest["weight"]:
        heaviest = people[i]
print(f"Pessoa mais pesada: {heaviest}")

lighter = people[0]
for i in range(3):
    if people[i]["weight"] < lighter["weight"]:
        lighter = people[i]
print(f"Pessoa mais leve: {lighter}")

