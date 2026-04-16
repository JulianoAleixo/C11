"""
By: Juliano Moreira Aleixo
https://julianoaleixo.dev
"""

import matplotlib.pyplot as plt
import seaborn as sns

ds_mpg = sns.load_dataset('mpg')

sns.set_style('darkgrid')
sns.set_context('notebook')
sns.regplot(data=ds_mpg, x='horsepower', y='mpg', line_kws={'color': 'red'})

plt.xlabel('Potência (horsepower)')
plt.ylabel('Consumo (mpg)')
plt.title('Relação entre Potência e Consumo de Combustível')
plt.show()
