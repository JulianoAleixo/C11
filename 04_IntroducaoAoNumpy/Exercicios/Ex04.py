"""
By: Juliano Moreira Aleixo
https://julianoaleixo.dev
"""

import numpy as np

rows_rand = np.random.randint(1, 10)
cols_rand = np.random.randint(1, 10)

mat = np.zeros((rows_rand, cols_rand))

rows, cols = mat.shape

if (rows * cols) % 2 == 0:
    print('Vetor unidimensional com número par de elementos.')
else:
    print('Vetor unidimensional com número ímpar de elementos.')
