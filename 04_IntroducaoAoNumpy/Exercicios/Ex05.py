"""
By: Juliano Moreira Aleixo
https://julianoaleixo.dev
"""

import numpy as np

np.random.seed(10)

mat = np.random.randint(1, 51, [4, 4])
print('Matriz: ')
print(mat)
print()

print('Média de cada linha e coluna: ')
rows_avg = np.mean(mat, axis=1)
cols_avg = np.mean(mat, axis=0)
for i in range(4):
    print(f'Linha {i}: {rows_avg[i]}')
    print(f'Coluna {i}: {cols_avg[i]}')
    print()

print('Maior valor entre as médias das linhas e das colunas: ')
max_avg_row = np.max(rows_avg)
max_avg_col = np.max(cols_avg)
print(f'Maior média das linhas: {max_avg_row}')
print(f'Maior média das colunas: {max_avg_col}')
print()

print('Quantidade de aparições de cada número:')
values, count = np.unique(mat, return_counts=True)
for i in range(len(values)):
    print(f"Número {values[i]}: {count[i]} vez(es)")
print()

print("Números que aparecem exatamente 2 vezes:")
for i in range(len(values)):
    if count[i] == 2:
        print(values[i])
