"""
By: Juliano Moreira Aleixo
https://julianoaleixo.dev
"""

import numpy as np

arr_ones = np.ones(8)
arr_randoms = np.random.randint(0, 10, 8)

arr_sum = arr_ones + arr_randoms

if arr_sum.sum() >= 40:
    arr_sum = arr_sum.reshape(4, 2)
else:
    arr_sum = arr_sum.reshape(2, 4)

print(arr_sum)
