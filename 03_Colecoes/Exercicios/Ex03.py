"""
By: Juliano Moreira Aleixo
https://julianoaleixo.dev
"""

student = {
    "name": "Juliano Moreira Aleixo",
    "grade": 80,
}

if student["grade"] >= 50:
    student["situation"] = "AP"
else:
    student["situation"] = "RP"

print(student)
