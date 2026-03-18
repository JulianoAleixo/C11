"""
By: Juliano Moreira Aleixo
https://julianoaleixo.dev
"""

import numpy as np

dataset = np.loadtxt('./Datasets/paises.csv', delimiter=';', dtype=str, encoding='utf-8-sig')

# ------------------------------------------------

df_sliced = dataset[0:, 0:4]
print(df_sliced)
print()

# ------------------------------------------------

regions = np.unique(dataset[1:, 1])
print(f'O dataset possui {len(regions)} regiões, sendo elas: ')
for region in regions:
    print(f'- {region}')
print()

# ------------------------------------------------

df_literacy = dataset[1:, 9].astype(float)
print(f'A taxa média de alfabetização é de {df_literacy.mean():.2f}%')
print()

# ------------------------------------------------

df_northern_america = dataset[1:][np.char.equal(dataset[1:, 1], 'NORTHERN AMERICA')]
print(f'A quantidade de países que são da América do Norte é: {len(df_northern_america)}')
print()

# ------------------------------------------------

df_latin_america_carib = dataset[1:][np.char.equal(dataset[1:, 1], 'LATIN AMER. & CARIB')]
idx_max_gdp = np.argmax(df_latin_america_carib[0:, 8])
print(f'O país da América do Sul & Caribe com a maior renda per capita é {df_latin_america_carib[idx_max_gdp][0]}')

# ------------------------------------------------
