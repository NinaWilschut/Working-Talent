print('Start met csv uitlees applicatie')

import pandas as pd

pokemon = pd.read_csv('pokemon.csv')

print(pokemon['Name'])

for i, row in pokemon.iterrows():
    name = row['Name']
    print(f'De naam van de pokemon is {name}')