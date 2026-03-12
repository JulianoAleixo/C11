"""
By: Juliano Moreira Aleixo
https://julianoaleixo.dev
"""

import numpy as np

dataset = np.loadtxt('./chocolate_sales_2025.csv', delimiter=',', dtype=str, encoding='utf-8-sig')

# ------------------------------------------------

df_milk_chocolates_prices = dataset[1:, 7][np.char.equal(dataset[1:, 3], 'Milk Chocolate')].astype(float)
print(f'A média de preço de um chocolate ao leite é de U${df_milk_chocolates_prices.mean():.2f}')

# ------------------------------------------------

countries, count_country = np.unique(dataset[1:, 4], return_counts=True)
idx_max_country = np.argmax(count_country)
print(f'O país com o maior número de registros é: {countries[idx_max_country]}')

# ------------------------------------------------

card_revenue = dataset[1:, 9][np.char.equal(dataset[1:, 6], 'Card')].astype(float)
card_revenue_with_fee = (card_revenue + (0.05 * card_revenue)).sum()
print(f'As operadoras de cartão faturaram U${card_revenue_with_fee:.2f}')

# ------------------------------------------------

brands, count_brand = np.unique(dataset[1:, 2], return_counts=True)
idx_max_brand = np.argmax(count_brand)
print(f'A marca com o maior número de registros é: {brands[idx_max_brand]}')

# ------------------------------------------------

total_sold = dataset[1:, 8].astype(int).sum()
print(f'O total de unidades de chocolates vendidos foi de {total_sold}')

# ------------------------------------------------
