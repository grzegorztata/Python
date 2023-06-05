import pandas as pd

exam1 = [89,85,93,83]
exam2 = [74,56,44,92]
exam3 = [67,59,79,84]
labels = ['Student A','Student B','Studnet C', 'Student D']
df = pd.DataFrame({'e1':exam1, 'e2':exam2, 'e3':exam3}, index=labels)
df['Semester1'] = df['e1'] + df['e2'] + df['e3']
print(df)

print('\n----- Zmiana nazw kolumn -----')
df_renamed = df.rename(columns={'e1':'exam1','e2':'exam2','e3':'exam3'})
print(df_renamed)

print('\n----- Zmiana nazwy indexu -----')
df_change_index = df.rename(index={'Studnet C':'Student C'})
print(df_change_index)

print('\n----- Zmiana wielkości liter kolumn -----')
df_upper_columns = df.rename(str.upper, axis='columns')
print(df_upper_columns)