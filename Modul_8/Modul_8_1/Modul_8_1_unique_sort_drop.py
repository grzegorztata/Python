import pandas as pd

df = pd.DataFrame({'A':[100,44,56,99,85,100],
                   'B':['Panda', 'Snake', 'Snake', 'Rat', 'Dog', 'Panda']})
print(df)

print('\n----- Wyciąganie unikalnych wartości z tabeli -----')
df_unique_A = df['A'].unique()
df_unique_B = df['B'].unique()
df_nunique_B = df['B'].nunique()  # nunique() - liczba wartości unikalnych. Tutaj 4

print(df_unique_A)
print(df_unique_B)
print(df_nunique_B)

print('\n----- Zliczanie liczby konkretnej wartości w kolumnie -----')
df_val_count_A = df['A'].value_counts()
df_val_count_B = df['B'].value_counts()

print(df_val_count_A)
print(df_val_count_B)

print('\n----- Wyświetlanie udziału procentowego wartości w kolumnie -----')
df_percent = df['B'].value_counts(normalize=True)

print(df_percent)

print('\n----- Sortowanie rosnąco i malejąco po kolumnie -----')
df_sort_asc = df.sort_values(by='A')
df_sort_desc = df.sort_values(by='A', ascending=False)

print(df_sort_asc)
print(df_sort_desc)

print('\n----- Usuwanie duplikatów -----')
df_drop_duplicates = df.drop_duplicates()

print(df_drop_duplicates)