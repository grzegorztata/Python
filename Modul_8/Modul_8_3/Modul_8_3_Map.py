# map - stosowana wyłącznie na obiektach typu series. Przyjmuje dict, Series lub callable
# apply  - na DataFrame i na Series. Przyjmuje wyłącznie callable

import pandas as pd
pivot_file = 'KursPython/Modul_8/Modul_8_3/Files/Pivot.xlsx'

df = pd.read_excel(pivot_file)

car_dict = dict(zip(df['Przedstawiciel'].unique(),['Mazda','Toyota','BMW','Audi','Fiat','Seat']))
print(car_dict)

# Dodanie samochodu do tabeli
df['Marka Samochodu'] = df['Przedstawiciel'].map(car_dict)
print(f'\n{df.sample(10)}')