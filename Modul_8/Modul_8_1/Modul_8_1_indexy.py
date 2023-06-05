import pandas as pd

exam1 = [89,85,93,83]
exam2 = [74,56,44,92]
exam3 = [67,59,79,84]
labels = ['Student A','Student B','Student C', 'Student D']
df = pd.DataFrame({'e1':exam1, 'e2':exam2, 'e3':exam3}, index=labels)
df['Semester1'] = df['e1'] + df['e2'] + df['e3']
print(df)

print('\n----- Ustawianie nowego indexu - Sposób 1 -----')
df_new_index = df.reset_index()
print(df_new_index)

df_new_index['student_name'] = ['Adrian', 'Bartłomiej', 'Celina', 'Dagmara']
print(f'\n {df_new_index}')

df_new_index_1 = df_new_index.set_index('student_name')
print(f'\n {df_new_index_1}')

print('\n----- Ustawianie nowego indexu - Sposób 2 -----')
df_new_index_2 = df.reset_index()
print(df_new_index_2)

df_new_index_2.index = ['Adrian', 'Bartłomiej', 'Celina', 'Dagmara']
print(df_new_index_2)