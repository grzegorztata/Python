import pandas as pd

# Wczytywanue danych z CSV
df = pd.read_csv('KursPython/Modul_8/Modul_8_2/myCsvFile.csv')

# Eksport danych do CSV
df.to_csv('myNewCsvFile.csv', index=False)