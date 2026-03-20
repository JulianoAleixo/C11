"""
By: Juliano Moreira Aleixo
https://julianoaleixo.dev
"""

import numpy as np
import pandas as pd

seriesAno1 = pd.Series({'Java': 16.25, 'C': 16.04, 'Python': 9.85})
seriesAno2 = pd.Series({'C': 16.21, 'Python': 12.12, 'Java': 11.68})

# -------------------------------------

print(f'A porcentagem das 3 linguagens no ano 1 é : {seriesAno1.sum()}%')
print(f'A porcentagem das 3 linguagens no ano 2 é : {seriesAno2.sum()}%')
print()

# -------------------------------------

seriesPassed = seriesAno2 - seriesAno1
print('O crescimento/declínio de cada linguagem de um ano para o outro foi: ')
print(seriesPassed)
print()

# -------------------------------------

seriesGrowing = seriesPassed[seriesPassed > 0]
print('As linguagens com crescimento são: ')
print(seriesGrowing)
print()

# -------------------------------------

seriesNext2Years = seriesAno2 + (seriesPassed * 2)
print(f'A linguagem mais popular daqui 2 anos será: {seriesNext2Years.nlargest(1).index[0]}')
print()

# -------------------------------------

np.random.seed(10)
df = pd.DataFrame(
    index=['A', 'B', 'C', 'D', 'E'],
    columns=['W', 'X', 'Y', 'Z'],
    data=np.random.randint(1, 50, [5, 4])
)
xLowerThen30 = df['X'][df['X'] < 30]
print(f'A média dos valores de X menores que 30 é {xLowerThen30.mean()}')
print()

# -------------------------------------

dMean = df.loc['D'].mean()
eSum = df.iloc[4].sum()
print(f'Média de D: {dMean}')
print(f'Soma de E: {eSum}')
print()

# -------------------------------------

sliced = df.loc[['A', 'C', 'E'], ['X', 'Y']]
print(sliced)
print()
print('Soma dos elementos por linha:')
print(sliced.sum(axis=1))
print()
print('Soma dos elementos por coluna:')
print(sliced.sum(axis=0))

# -------------------------------------
