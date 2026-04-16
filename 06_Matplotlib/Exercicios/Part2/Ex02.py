"""
By: Juliano Moreira Aleixo
https://julianoaleixo.dev
"""

import matplotlib.pyplot as plt
import seaborn as sns

ds_titanic = sns.load_dataset('titanic')

sns.set_style('darkgrid')
sns.set_context('notebook')
sns.histplot(data=ds_titanic, x='age', hue='sex', kde=True)

plt.xlabel('Idade')
plt.ylabel('Contagem')
plt.title('Distribuição de Idades dos Passageiros por Sexo – Titanic')
plt.show()
