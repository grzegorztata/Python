import pandas as pd 
import numpy as np

exam1 = [89,85,93,83]
exam2 = [74,56,44,92]
labels  = ['Student A', 'Student B', 'Student C', 'Student D']

e1 = pd.Series(exam1, labels)
e2 = pd.Series(exam2, labels)

df = pd.DataFrame({'e1':exam1, 'e2':exam2}, index=labels)
print(df)

print('\n----- Wykorzystanie ndarray -----')
data = np.array([exam1,exam2])
print(data.transpose())
df1 = pd.DataFrame(data.transpose(), index=labels, columns=['e1','e2'])
print(df1)

print('\n----- Konwersja DataFrame na ndarray -----')
print(df1.to_numpy())

print('\n----- Dodanie kolumny -----')
df['e3'] = [67,59,79,84]
print(df)

print('\n----- Dodanie kolumny podsumowania -----')
df['Semester1'] = df['e1'] + df['e2'] + df['e3']
print(df)

print('\n----- Wyświetlanie kilku kolumn -----')
print(df[['e1','e2']])

print('\n----- Wyświetlanie informacji dla pojedyńczej labelki -----')
print(df.loc['Student C'])

print('\n----- Wyświetlanie informacji dla pojedyńczej labelki i pojedyńczej kolumny -----')
print(df.loc['Student C', 'e2'])

print('\n----- Wyświetlanie pandas + fancy indexing -----')
print(df.loc[['Student C','Student D'], ['e2']])

print('\n----- Odniesienie się do pozycji zamiast labelki -----')
print(df.iloc[1])

print('\n----- Slicing z funkcją iloc() -----')
print(df.iloc[1:,1])