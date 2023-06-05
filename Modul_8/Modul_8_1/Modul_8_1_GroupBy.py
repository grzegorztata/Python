import pandas as pd

df = pd.DataFrame({'Category':['Games','Games','Games',

                               'Film&Video','Film&Video','Film&Video'],

                  'Project_Title':['The Last Faith','Magic Puzzles','Dinosaur Fossil Hunter',

                                   'Beyond Your Eyes','5150','8-Bit Wars'],

                  'Pledged':[92774,2873519,7962,

                             276,23963,6950],

                  'Country':['UK','USA','Poland',

                             'Bulgaria','USA','UK'],

                  'Date_Start':['2020-03-21','2020-03-11','2020-04-16',

                                '2020-02-09','2020-04-10','2020-03-19']})

print(df)

print('\n----- Suma dotacji dla kategorii -----')
df_sum = df.groupby('Category').sum('Pledged')
print(df_sum)

print('\n----- Średnia dotacji dla kategorii -----')
df_average = df.groupby('Category').mean('Pledged')
print(df_average)

print('\n----- Liczba projektów dla każdej kategorii -----')
df_count = df.groupby('Category').count()
print(df_count)

print('\n----- Sumowanie dotacji dla poszczególnych miesięcy -----')
df['Date_Start'] = pd.to_datetime(df['Date_Start'])
df_for_months = df.groupby(pd.Grouper(key='Date_Start', freq='M')).sum('Pledged')
print(df_for_months)

print('\n----- Sumowanie dotacji i liczby projektów dla poszczególnych miesięcy -----')
# agg - sposób agregowania każdej kolumny
df_for_columns = df.groupby(pd.Grouper(key='Date_Start', freq='M')).agg({'Pledged':'sum','Project_Title':'count'})
print(df_for_columns)

print('\n----- Grupowanie po więcej niż jednej kolumnie -----')
df_for_more_columns = df.groupby(['Country', 'Category']).sum('Pledged')
print(df_for_more_columns)