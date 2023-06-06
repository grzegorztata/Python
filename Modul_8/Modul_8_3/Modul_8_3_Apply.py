import pandas as pd
import numpy as np
import math
pivot_file = 'KursPython/Modul_8/Modul_8_3/Files/Pivot.xlsx'

df = pd.read_excel(pivot_file)
print(df.head())

def commission_fee(x):
    if x <= 300:
        return 0
    elif x <= 900:
        return x * 0.03
    else:
        return x * 0.06
    
# Dodanie commission_fee do tabeli. Apply - wywołanie specjalnie utworzonej funkcji
df['commission_fee'] = df['Sprzedaż'].apply(lambda x: commission_fee(x))
print(f'\n{df.head()}')

# Apply - dodawanie wbudowanych funkcji pythona. Dodanie kolumny z długością znaków w produkcie
df['Produkt_len'] = df['Produkt'].apply(len)
print(f'\n{df.head()}')

# Apply - przy lambdzie. Tutaj zliczanie liczby opakowań (5 sztuk w opakowaniu)
df['#_opakowań'] = df['Sztuki'].apply(lambda x: math.ceil(x/5)) # math.ceil() - zaokrąglenie w górę
print(f'\n{df.head()}')

# Apply przy wykorzystaniu obliczeń dla więcej niż jednej kolumny
# Tutaj bonus 200 przy rentowności 55%
def bonus(row):
    margin = (row['Sprzedaż'] - row['Koszty'])/row['Sprzedaż']
    if margin > 0.55:
        return 200
    else:
        return 0
    
df['Bonus'] = df.apply(lambda row: bonus(row),axis=1)
print(f'\n{df.sample(10)}')  # sample(10) - 10 randomowych rzędów