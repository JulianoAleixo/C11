"""
By: Juliano Moreira Aleixo
https://julianoaleixo.dev
"""

import numpy as np
import matplotlib.pyplot as plt

dataset = np.loadtxt('../Datasets/space.csv', delimiter=';', dtype=str, encoding='utf-8-sig')

eua_companies = np.unique(dataset[np.char.find(dataset[1:, 2], 'USA')][:, 1])
china_companies = np.unique(dataset[np.char.find(dataset[1:, 2], 'China')][:, 1])

countries = ['EUA', 'China']
quantities = [len(eua_companies), len(china_companies)]

plt.bar(countries, quantities, color=['blue', 'red'])

plt.title('Quantidade de Empresas Espaciais')
plt.ylabel('Número de Empresas')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
