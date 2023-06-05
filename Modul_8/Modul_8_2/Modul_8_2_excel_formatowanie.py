import pandas as pd


df = pd.read_excel('KursPython/Modul_8/Modul_8_2/myExcelFile.xlsx', sheet_name='my_data')

writer = pd.ExcelWriter('KursPython/Modul_8/Modul_8_2/conditional_format.xlsx', engine='xlsxwriter')

df.to_excel(writer, sheet_name='my_conditional')

workbook = writer.book
worksheet = writer.sheets['my_conditional']

format1 = workbook.add_format({'bg_color':   '#FFC7CE',
                               'font_color': '#9C0006'})

worksheet.conditional_format("C2:C12",{'type': 'cell',
                                      'criteria':'>=',
                                      'value':3,
                                      'format':format1})

worksheet.write_string('A16','Podaj liczbę całkowitą większą od 0:')

worksheet.data_validation('B16', {
    'validate':'integer',
    'criteria':'>',
    'value':0
})

worksheet.set_column('A:A',35)  # Rozszerzenie kolumny 

writer._save()
workbook.close()