"""
By: Juliano Moreira Aleixo
https://julianoaleixo.dev
"""

import pandas as pd

df = pd.read_csv('./Datasets/paises.csv', delimiter=';')

df.columns = df.columns.str.strip()
df['Region'] = df['Region'].str.strip()
df['Country'] = df['Country'].str.strip()

# --------------------------------------------------------------

oceania = df[df['Region'].str.contains('OCEANIA', case=False, na=False)]

print("Países da OCEANIA:")
print(oceania['Country'].to_string(index=False))
print()
print(f"Quantidade de países da OCEANIA: {len(oceania)}")
print()

# --------------------------------------------------------------

largest_population = df.loc[df['Population'].idxmax(), ['Country', 'Region']]
print(f"País com maior população: {largest_population['Country']}")
print(f"Região com maior população: {largest_population['Region']}")
print()

# --------------------------------------------------------------

mean_literacy = df.groupby('Region')['Literacy (%)'].mean().round(2)
print("Média de Alfabetização (%) por Região:")
print(mean_literacy.to_string())
print()

# --------------------------------------------------------------

no_coast = df[df['Coastline (coast/area ratio)'] == 0][['Country']]
no_coast.to_csv('./Outputs/noCoast.csv', index=False)
print(f"{len(no_coast)} países sem costa marítima salvos em noCoast.csv")
print(no_coast['Country'].to_string(index=False))
print()

# --------------------------------------------------------------


def classify_deathrate(deathrate):
    if deathrate < 9:
        return 'Balanced'
    else:
        return 'Urgent'


df['Humanitarian Help'] = df['Deathrate'].apply(classify_deathrate)
print("Dataset com coluna 'Humanitarian Help':")
print(df[['Country', 'Deathrate', 'Humanitarian Help']].head(20).to_string(index=False))
print()

# --------------------------------------------------------------
