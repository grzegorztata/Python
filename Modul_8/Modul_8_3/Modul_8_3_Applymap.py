# Używamy w sytuacji wymagającej wykonania tej samej transformacji na wielu kolumnach i wierszach jednocześnie (df)

import pandas as pd
pivot_file = 'KursPython/Modul_8/Modul_8_3/Files/Pivot.xlsx'

df = pd.read_excel(pivot_file)

# Zamiana wszystkich wartości na tabeli z wielkiej litery
df = df.applymap(lambda x: x.upper() if isinstance(x, str) else x)
print(f'\n{df.sample(10)}')