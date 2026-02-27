"""
By: Juliano Moreira Aleixo
https://julianoaleixo.dev
"""

import numpy as np

arr_1 = np.arange(0, 52, 2)
arr_2 = np.arange(100, 49, -2)

arr_result = np.sort(np.concatenate((arr_1, arr_2)))

print(arr_result)
