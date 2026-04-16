"""
By: Juliano Moreira Aleixo
https://julianoaleixo.dev
"""

import numpy as np
import matplotlib.pyplot as plt

dataset = np.loadtxt('../Datasets/paises.csv', delimiter=';', dtype=str, encoding='utf-8-sig')
df_northern_america = dataset[1:][np.char.equal(dataset[1:, 1], 'NORTHERN AMERICA')]
countries = df_northern_america[:, 0]

death_rate = df_northern_america[:, 15].astype(float)
birth_rate = df_northern_america[:, 16].astype(float)

plt.figure(figsize=(10, 6))

plt.plot(countries, birth_rate, marker='o', label='Taxa de Natalidade', color='blue')
plt.plot(countries, death_rate, marker='s', label='Taxa de Mortalidade', color='red')

plt.title('Taxas de Natalidade e Mortalidade - América do Norte')
plt.xlabel('Países')
plt.ylabel('Taxa')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()
