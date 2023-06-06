import pandas as pd

pivot_file = 'KursPython/Modul_8/Modul_8_3/Files/Pivot.xlsx'

df = pd.read_excel(pivot_file)

##### dt - DataTime #####
df['Data'] = pd.to_datetime(df['Data'])
df['Data'].dt.day_name().head()  # dzień tygodnia
df['Data'].dt.month_name().head()  # miesiąc
df['Data'].dt.is_month_start.head()  # True/False w zależności czy data jest początkiem miesiąca

# Filtrowanie
filter_thursday = df[df['Data'].dt.day_name()=='Thursday'].head()
print(f'\n{filter_thursday}')



##### str #####
# Upper na pojedyńczym obiekcie str
upper_product = df['Produkt'].str.upper().head()
print(f'\n{upper_product}')

# Filtrowanie wierszy w tabeli (True/False)
region_ends_with = df['Region'].str.endswith('ód').head()
print(f'\n{region_ends_with}')

# Filtrowanie z contains()
region_contains = df[df['Region'].str.contains('Zachód')].sample(10)
print(f'\n{region_contains}')