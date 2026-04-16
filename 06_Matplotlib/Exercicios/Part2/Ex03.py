"""
By: Juliano Moreira Aleixo
https://julianoaleixo.dev
"""

import matplotlib.pyplot as plt
import seaborn as sns

ds_titanic = sns.load_dataset('titanic')

sns.set_style('whitegrid')
sns.set_context('notebook')

sns.boxplot(data=ds_titanic, x='pclass', y='age', hue='sex')

plt.xlabel('Classe')
plt.ylabel('Idade')
plt.title('Distribuição de Idades por Classe e Sexo – Titanic')
plt.show()
