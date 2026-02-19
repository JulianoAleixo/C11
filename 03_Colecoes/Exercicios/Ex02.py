"""
By: Juliano Moreira Aleixo
https://julianoaleixo.dev
"""

store1 = {"iphone", "galaxy", "nokia"}
store2 = {"xiaomi", "huawei", "nokia"}

print("Modelos ao todo: ")
print(store1.union(store2))

print()
print("Modelos de ambas as lojas: ")
print(store1.intersection(store2))
