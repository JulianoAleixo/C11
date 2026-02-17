"""
By: Juliano Moreira Aleixo
https://julianoaleixo.dev
"""

name = input("Digite seu nome: ")

print(f"- Seu nome em maiúsculo:  {name.upper()}")
print(f"- Seu nome em minúsculo: {name.lower()}")
print(f"- Quantidade de letras do seu nome: {len(name)}")
print(f"- Quantidade de letras do seu nome: {len(name)}")

new_name = name.split(" ")
new_name[-1] = "do Inatel"
new_name = " ".join(new_name)
print(f"- Seu novo nome é {new_name}")
