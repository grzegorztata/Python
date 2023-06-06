import pandas as pd
import numpy as np
pivot_file = 'KursPython/Modul_8/Modul_8_3/Files/Pivot.xlsx'

df = pd.read_excel(pivot_file)
print(df.head())  # head zwraca 5 pierwszych rzędów

pivot_table = df.pivot_table(values='Sprzedaż',index='Przedstawiciel',columns='Region',aggfunc=np.sum)  #aggfunc - domyślnie (puste) jest średnia
print(f'\n{pivot_table}')

pivot_table_with_zeros = df.pivot_table(values='Sprzedaż',index='Przedstawiciel',columns='Region',aggfunc=np.sum).fillna(0).round(2)
print(f'\n{pivot_table_with_zeros}')

pivot_table_two_indexes = df.pivot_table(values='Sprzedaż',index=['Region','Przedstawiciel'],aggfunc=np.sum).round(2)
print(f'\n{pivot_table_two_indexes}')

pivot_table_min_max = df.pivot_table(values='Sprzedaż',index='Region',aggfunc=[len,np.max,np.min]).round(0)
print(f'\n{pivot_table_min_max}')