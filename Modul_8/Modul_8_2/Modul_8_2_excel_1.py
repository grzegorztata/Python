import pandas as pd
import xlsxwriter

df = pd.read_excel('KursPython/Modul_8/Modul_8_2/myExcelFile.xlsx', sheet_name='my_data')

writer = pd.ExcelWriter('KursPython/Modul_8/Modul_8_2/add_chart.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='my_chart')

workbook = writer.book
worksheet = writer.sheets['my_chart']

chart = workbook.add_chart({'type':'line'})

def grab_series(df, sheet_name, colname, startcol=0, startrow=0):

    col_index = df.columns.tolist().index(colname)
    col_letter = chr(ord('@')+(col_index+2+startcol))
    first_row = startrow + 2
    last_row = startrow + 1 + len(df)
    return f"='{sheet_name}'!{col_letter}{first_row}:{col_letter}{last_row}"

chart.add_series({'values': grab_series(df, 'my_chart', 'B')})

chart.set_x_axis({
    'name': 'x^2',
    'name_font': {'size': 14, 'bold': True},
    'num_font':  {'italic': True },
})

chart.set_legend({'none': True})

worksheet.insert_chart('F2', chart)

writer._save()
workbook.close()