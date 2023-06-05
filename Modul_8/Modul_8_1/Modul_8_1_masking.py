import pandas as pd 
import numpy as np

exam1 = [89,85,93,83]
exam2 = [74,56,44,92]
exam3 = [67,59,79,84]
labels  = ['Student A', 'Student B', 'Student C', 'Student D']
df = pd.DataFrame({'e1':exam1, 'e2':exam2, 'e3':exam3}, index=labels)
df['Semester1'] = df['e1'] + df['e2'] + df['e3']
# print(df)

print('\n----- Masking True/False -----')
mask = df['e2'] > 70
print(mask)

print('\n----- Filtrowanie wartości -----')
mask_filter = df[df['e2'] > 70]
print(mask_filter)

print('\n----- Filtrowanie wartości z operatorem logicznym -----')
mask_filter_1 = df[(df['e2']<50) | (df['e2']>90)]
print(mask_filter_1)