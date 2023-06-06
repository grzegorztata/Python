import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Ad.1 - Zaimportuj plik csv
df = pd.read_csv('KursPython/Modul_8/Zadania_8/Files/fatal-police-shootings-data.csv')
print(df.head())

# Ad.2 - Przekształć tabelę w taki sposób, 
# aby wskazywała zestawienie jednocześnie liczby ofiar interwencji według rasy (‘race’) oraz tego, 
# czy wykazywały one oznaki choroby psychicznej (‘signs_of_mental_illness’).
# aggfunc='size'
pivot_table = df.pivot_table(index='race', columns='signs_of_mental_illness', aggfunc='size', fill_value=0)
print(pivot_table)

# Ad.3a - Dodaj do tego zestawienia kolumnę wskazującą 
# jaki odsetek ofiar interwencji wykazywało oznaki choroby psychicznej dla każdej z ras
# a / (a + b)
pivot_table['% True'] = pivot_table.apply(lambda row: row[True] * 100 / (row[True] + row[False]), axis=1).round(1)
print(f'\n{pivot_table}')

# Ad.3b - Odpowiedz, która z nich charakteryzuje się największym odsetkiem znamion choroby psychicznej podczas interwencji
max_illnessess_true = pivot_table['% True'].idxmax()
print(f'\nRasa z najwyższym odsetkiem chorób psychicznych w tym zestawieniu to: {max_illnessess_true}')

# Ad.4a - Dodaj kolumnę oznaczającą dzień tygodnia, w którym doszło do interwencji.
df['date'] = pd.to_datetime(df['date'])
df['weekday'] = df['date'].dt.day_name()

# Ad.4b - Zlicz interwencje według odpowiedniego dnia tygodnia
""" weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
accidents_by_weekday = df['weekday'].value_counts().sort_values
accidents_by_weekday.columns = ['weekday', 'liczba']
print(f'\n{accidents_by_weekday}') """
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df['weekday'] = pd.Categorical(df['weekday'], categories=weekday_order, ordered=True)  # innego sortowania dni tygodnia nie znalazłem
accidents_by_weekday = df['weekday'].value_counts().sort_index()
# print(f'\n{accidents_by_weekday}')
writer = pd.ExcelWriter('KursPython/Modul_8/Zadania_8/Files/accidents_by_weekdays.xlsx', engine='xlsxwriter')
accidents_by_weekday.to_excel(writer, sheet_name='weekdays')
writer._save()
writer.close()

# Ad.4c - Utwórz wykres kolumnowy dla incydentów dla poszczególnych dni tygodnia
data = pd.read_excel('KursPython/Modul_8/Zadania_8/Files/accidents_by_weekdays.xlsx', sheet_name='weekdays')
workbook = writer.book
worksheet = writer.sheets['weekdays']

chart = workbook.add_chart({'type': 'line'})

chart.add_series({
    'name': 'Incidents',
    'categories': '=weekdays!$A$2:$A$8',
    'values': '=weekdays!$B$2:$B$8',
})

chart.set_title({'name': 'Accidents by Weekday'})
chart.set_x_axis({'name': 'Weekday'})
chart.set_y_axis({'name': 'Number of Accidents'})

worksheet.insert_chart('D2', chart)

writer._save()
workbook.close()