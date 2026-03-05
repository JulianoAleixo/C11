"""
By: Juliano Moreira Aleixo
https://julianoaleixo.dev
"""

import numpy as np

dataset = np.loadtxt('./Datasets/space.csv', delimiter=';', dtype=str, encoding='utf-8-sig')

# ------------------------------------------------

df_status = dataset[1:, 7]
qtd_success = np.sum(df_status == 'Success')
qtd_total = len(df_status)
percentage = (qtd_success / qtd_total) * 100

print(f'Porcentagem de missões que deram certo: {percentage:.2f}%')
print()

# ------------------------------------------------

df_cost = dataset[1:, 6].astype(float)
df_cost = df_cost[df_cost > 0]
mean_cost = np.mean(df_cost)

print(f'Média de gastos nas missões espaciais: ${mean_cost:.2f}')
print()

# ------------------------------------------------

df_usa_missions = dataset[np.char.find(dataset[1:, 2], 'USA')]
print(f'Quantidade de missões feitas pelos EUA: {len(df_usa_missions)}')
print()

# ------------------------------------------------

df_spacex_missions = dataset[1:][np.char.equal(dataset[1:, 1], 'SpaceX')]
df_spacex_costs = df_spacex_missions[:, 6].astype(float)
most_expensive_mission = df_spacex_missions[np.argmax(df_spacex_costs)]
print(f'Missão mais cara da SpaceX: {most_expensive_mission}')
print()

# ------------------------------------------------

companies = np.unique(dataset[1:, 1])
for company in companies:
    qtd_company_missions = len(dataset[1:][np.char.equal(dataset[1:, 1], company)])
    print(f'{company} fez {qtd_company_missions} missão(ões).')
