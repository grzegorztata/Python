import pandas as pd
import xlsxwriter

df = pd.read_excel('KursPython/Modul_8/Modul_8_2/myExcelFile.xlsx', sheet_name='my_data')

# Zapisanie i zmiana sheetu
# df.to_excel('KursPython/Modul_8/Modul_8_2/myExcelFile.xlsx', sheet_name='my_new_data')

# Dodanie nowego pliku
# writer = pd.ExcelWriter('KursPython/Modul_8/Modul_8_2/pandas_simple.xlsx', engine='xlsxwriter')

# Dodanie kolejnych wartości do arkusza
# df = pd.DataFrame()
""" writer = pd.ExcelWriter('KursPython/Modul_8/Modul_8_2/pandas_simple.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='my_dfs')
df.to_excel(writer, sheet_name='my_dfs', startcol=6, startrow=5, index=False)
writer._save()  # '_save' zamiast 'save' """

writer = pd.ExcelWriter('KursPython/Modul_8/Modul_8_2/many_sheets.xlsx', engine='xlsxwriter')

df.to_excel(writer, sheet_name='my_df1')
df.to_excel(writer, sheet_name='my_df2')

writer._save()