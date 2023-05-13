import random
from faker import Faker

fake = Faker()
genres = ['Comedy', 'Drama', 'Thriller', 'Romance', 'Horror']


class Movies:

  def __init__(self, title, year, genre, views):
    self.title = title
    self.year = year
    self.genre = genre
    self.views = views

  def play(self, step=1):
    self.views += step


class Series(Movies):

  def __init__(self, episode, season, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.episode = episode
    self.season = season


movies_and_series = []

for i in range(10):
  title = fake.sentence(nb_words=3)
  year = random.randint(2000, 2023)
  genre = random.choice(genres)
  views = random.randint(1, 1000)
  movie = Movies(title=title, year=year, genre=genre, views=views)
  movies_and_series.append(movie)

for i in range(10):
  title = fake.sentence(nb_words=3)
  year = random.randint(2000, 2023)
  genre = random.choice(genres)
  views = random.randint(1, 1000)
  season = random.randint(1, 5)
  episode = random.randint(1, 20)
  series = Series(title=title, year=year, genre=genre, views=views, season=season, episode=episode)
  movies_and_series.append(series)

movies_and_series_by_title = sorted(movies_and_series,
                                    key=lambda films: films.title)

def get_series():
  for item in movies_and_series_by_title:
    if isinstance(item, Series):
      print(f'{item.title} S{item.season:02d}E{item.episode:02d}')
#      print(f'{item.title} S{item.season:02d}E{item.episode:02d} --- {item.views}')

def get_movies():
  for item in movies_and_series_by_title:
    if isinstance(item, Movies) and not isinstance(item, Series):
      print(f'{item.title} ({item.year})')
#      print(f'{item.title} ({item.year}) --- {item.views}')

def search(title):
  for item in movies_and_series_by_title:
    if item.title == title:
      if isinstance(item, Series):
        print(f'Serial "{item.title}" znajduje się w katalogu')
      elif isinstance(item, Movies):
        print(f'Film "{item.title}" znajduje się w katalogu')
      return
  print(f'"{title}" nie znajduje się w katalogu.')


def generate_view():
  for item in movies_and_series:
    views_number = random.randint(1, 100)
    item.play(step=views_number)

def play_ten_times():
  for i in range(10):
    generate_view()

def top_titles():
  top_views = sorted([(item, item.views) for item in movies_and_series], key=lambda x: x[1], reverse=True)[:3]
  return [f"{item[0].title} ({item[0].year}) - {item[1]} views" if isinstance(item[0], Movies) and not isinstance(item[0], Series) else f"{item[0].title} S{item[0].season:02d}E{item[0].episode:02d} - {item[1]} views" if isinstance(item[0], Series) else "" for item in top_views]
  # x: x[1] - sortowanie po item[1]
  # SyntaxError: expected 'else' after 'if' expression
  # Dodano 'and not isinstance(item[0], Series)''. Bez tego pokazuje rok dla seriali

print("----- BIBLIOTEKA FILMÓW -----")
print("     Filmy")
get_movies()
print("\n     Seriale")
get_series()

print("\n----- Wyszukiwarka -----")
search(movies_and_series[0].title)
search("Harry Potter")

# generate_view()
play_ten_times()
print("\n----- BIBLIOTEKA FILMÓW PO DODANIU WYŚWIETLEŃ -----")
for item in movies_and_series:
  if isinstance(item, Series):
    print(f'{item.title} (S{item.season:02d}E{item.episode:02d}) - {item.views} views')
  elif isinstance(item, Movies):
    print(f'{item.title} ({item.year}) - {item.views} views')

top_titles()
print("\n----- TOP 3 -----")
top_titles_list = top_titles()
for item in top_titles_list:
    print(item)