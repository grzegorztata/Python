import pandas as pd
import numpy as np
import missingno as msno

df_with_nulls = pd.DataFrame({'A':[1,100,np.nan,1000,10000],
                             'B':[2,4,2,4,np.nan],
                             'C':[40,np.nan,20,np.nan,np.nan]})

print(df_with_nulls)

print('\n----- Wyświetlanie wartości procentowej i liczbowej dla wartości pustych -----')
print(df_with_nulls.isnull().mean())
print()
print(df_with_nulls.isnull().sum())

print('\n----- Wyfiltrowanie wartości NaN dla kolumny C')
nulls_for_c = df_with_nulls[df_with_nulls['C'].isnull()]
print(nulls_for_c)

print('\n----- DROPNA - usunięcie wszystkich rzędów zawierających NaN -----')
df_dropna = df_with_nulls.dropna()
print(df_dropna)  # powinien zostać tylko rząd 0

print('\n----- Thresh - Wybieranie minimalnej liczby NaN, które zostaną wyświetlone przy dropna() -----')
df_dropna_thrash = df_with_nulls.dropna(thresh=2)
print(df_dropna_thrash)

print('\n----- Thresh dla kolumn -----')
df_dropna_columns = df_with_nulls.dropna(thresh=3, axis=1)
print(df_dropna_columns)

print('\n----- FILLNA - uzupełnianie statyczne NaN')
df_fillna = df_with_nulls.fillna('NOWA WARTOŚĆ')
print(df_fillna)

print('\n----- FILLNA - Wartość dynamiczna (średnia)')
df_fillna_average = df_with_nulls['B'].fillna(df_with_nulls['B'].mean())
print(df_fillna_average)

print('\n----- backfill (uzupełnianie kolejną wartością) i ffill (uzupełnianie poprzednią wartością) -----')
df_fillna_backfill = df_with_nulls.fillna(method='backfill')
df_fillna_ffill = df_with_nulls.fillna(method='ffill')
print(df_fillna_backfill)
print(df_fillna_ffill)