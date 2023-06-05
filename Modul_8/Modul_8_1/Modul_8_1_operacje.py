import pandas as pd
import numpy as np

exam1 = [89,85,93,83]
exam2 = [74,56,44,92]
exam3 = [67,59,79,84]
labels  = ['Student A', 'Student B', 'Student C', 'Student D']
df = pd.DataFrame({'e1':exam1, 'e2':exam2, 'e3':exam3}, index=labels)
df['Semester1'] = df['e1'] + df['e2'] + df['e3']
print(df)

print('\n----- Usuwanie kolumn -----')
df1 = df.drop('Semester1',axis=1)  # pamiętać o axis. Domyślnie mamy '0' - czyli wiersze, '1' - to są  kolumny
print(df1)

print('\n----- Usuwanie kolumn z df bez potrzeby tworzenia nowej zmiennej (Inplace)-----')
df.drop(['e3', 'Semester1'], axis=1, inplace=True)
print(df)

print('\n----- Usuwanie wierszy z df bez potrzeby tworzenia nowej zmiennej (Inplace)-----')
df.drop('Student B', inplace=True)
print(df)

print('\n----- Resetowanie indexu -----')
df.reset_index(inplace=True)
print(df)