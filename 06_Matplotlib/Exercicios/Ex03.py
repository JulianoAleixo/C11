"""
By: Juliano Moreira Aleixo
https://julianoaleixo.dev
"""

import numpy as np
import matplotlib.pyplot as plt

dataset = np.loadtxt('./Datasets/space.csv', delimiter=';', dtype=str, encoding='utf-8-sig')

df_roscosmos_missions = dataset[1:][np.char.equal(dataset[1:, 1], 'Roscosmos')]
status = df_roscosmos_missions[:, 7]
total_success = np.sum(status == 'Success')
total_failures = len(status) - total_success

labels = ['% Sucesso', '% Falha']
quantities = [total_success, total_failures]

plt.pie(x=quantities, labels=labels, autopct='%1.1f%%')
plt.title('Missões da Roscosmos: Sucesso vs Falha')

plt.show()
