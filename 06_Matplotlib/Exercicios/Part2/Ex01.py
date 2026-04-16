"""
By: Juliano Moreira Aleixo
https://julianoaleixo.dev
"""

import matplotlib.pyplot as plt
import seaborn as sns

ds_iris = sns.load_dataset('iris')
ds_setosa = ds_iris[ds_iris['species'] == 'setosa']

corr = ds_setosa[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].corr()

sns.set_style('whitegrid')
sns.set_context('notebook')
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm')

plt.title('Correlação entre Variáveis – Iris Setosa')
plt.tight_layout()
plt.show()
