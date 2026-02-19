"""
By: Juliano Moreira Aleixo
https://julianoaleixo.dev
"""

n = int(input("Digite a quantidade de pessoas: "))

people = []
for i in range(n):
    name = input(f"Digite o nome da {i + 1}ª pessoa: ")
    age = int(input(f"Digite a idade da {i + 1}ª pessoa: "))
    while 1:
        sex = input(f"Digite o sexo da {i + 1}ª pessoa (M/F): ").upper()
        if sex in ['M', 'F']:
            break

    person = {"name": name, "age": age, "sex": sex}
    people.append(person)
    print()

total_age = 0
women_with_less_then_20 = 0
for person in people:
    total_age += person["age"]
    if person["age"] < 20 and person["sex"] == 'F':
        women_with_less_then_20 += 1

print(f"Media de idade do grupo: {(total_age / n):.2f}")
print(f"Quantidade de mulheres com menos de 20 anos: {women_with_less_then_20}")
