import pandas as pd

data = pd.read_html('https://www.officialcharts.com/chart-news/the-best-selling-albums-of-all-time-on-the-official-uk-chart__15551/', header=0)
df = data[0]

writer = pd.ExcelWriter('KursPython/Modul_8/Zadania_8/Files/best_artists.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='artists')

# Ad.1 - Zmiana headerów na tłumaczenie polskie
new_headers = ['','TYTUŁ','ARTYSTA','ROK','MAX POZ']
df.columns = new_headers
writer = pd.ExcelWriter('KursPython/Modul_8/Zadania_8/Files/best_artists.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='artists')

# Ad.2 - Zliczanie wartości unikalnych w kolumnie D (Artysta)
unique_artists_count = df['ARTYSTA'].nunique()
print(f'Liczba unikalnych artystów: {unique_artists_count}')

# Ad.3 - Najczęściej występujący artysta (.idxmax() - zwraca najczęstszą wartość)
most_popular_artist = df['ARTYSTA'].value_counts().idxmax()
print(f'Artysta, który występuje najczęściej na liście to: {most_popular_artist}')

# Ad.4 - Nagłówki rozpoczynają się z wielkiej litery, pozostałe litery są małe (str.capitalize())
# df.columns = df.rename(str.capitalize, axis='columns') - dopytać
df.columns = df.columns.str.capitalize()
df.to_excel(writer, sheet_name='artists')

# Ad.5 - Wyrzuć z tabeli kolumnę 'Max poz'
df = df.drop('Max poz',axis=1)
df.to_excel(writer, sheet_name='artists')

# Ad.6 - W którym roku wyszło najwięcej albumów
albums_in_year = df['Rok'].value_counts().idxmax()
print(f'Najwięcej albumów wyszło w roku: {albums_in_year}')

# Ad.7 - Liczba albumów wydanych pomiędzy 1960 a 1990 'df[(df['e2']<50)|(df['e2']>90)]' + shape[0] (liczba rzędów)
albums_in_range = df[(df['Rok']>=1960)&(df['Rok']<=1990)].shape[0]
print(f'Liczba albumów wydanych w latach 1960-1990 to: {albums_in_range}')

# Ad.8 - W którym roku został wydany najmłodszy album na liście
youngest_album = df['Rok'].max()
print(f'Najmłodszy album z listy został wydany w roku: {youngest_album}')

writer = pd.ExcelWriter('KursPython/Modul_8/Zadania_8/Files/best_artists.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='artists')
writer._save()

# Ad.9 - Przygotuj listę najwcześniej wydanych albumów każdego artysty, który znalazł się na liście.
# Tutaj postanowiłem posortować po kolumnach 'Artysta' i 'Rok' a następnie usunąłem duplikaty w kolumnie 'Artysta'
sorted_artists = df.sort_values(['Artysta', 'Rok'])
oldest_albums_for_artist = sorted_artists.drop_duplicates(subset='Artysta', keep='first')
only_artist_and_year = oldest_albums_for_artist.drop(['','Tytuł'],axis=1)
only_artist_and_year.to_csv('KursPython/Modul_8/Zadania_8/Files/oldest_albums.csv', index=False)
#print(only_artist_and_year)

writer.close()

