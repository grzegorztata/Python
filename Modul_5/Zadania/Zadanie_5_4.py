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
        
        # Variables
        self.current_view = 0
        
    def play(self, step=1):
        self.current_view += step
        
"""     def __str__(self):
        return f'{self.title} ({self.year})' """
    
        
class Series(Movies):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season
        
"""     def __str__(self):
        return f'{self.title} S{self.season:02d}E{self.episode:02d}' """
    
# movie = Movies(title=fake.sentence(nb_words=3), year=random.randint(2000, 2023), genre=random.choice(genres), views=random.randint(0, 10000))

movies_and_series = []

for i in range(5):
    title = fake.sentence(nb_words=3)
    year = random.randint(2000, 2023)
    genre = random.choice(genres)
    views = random.randint(1, 10000)
    movie = Movies(title=title, year=year, genre=genre, views=views)
    movies_and_series.append(movie)

for i in range(1):
    title = fake.sentence(nb_words=3)
    year = random.randint(2000, 2023)
    genre = random.choice(genres)
    views = random.randint(1, 10000)
    season = random.randint(1, 5)
    episode = random.randint(1, 20)
    series = Series(title=title, year=year, genre=genre, views=views, season=season, episode=episode)
    movies_and_series.append(series)
    
movies_and_series_by_title = sorted(movies_and_series, key=lambda films: films.title)
    
""" for item in movies_and_series:
    print(item) """
    
def get_series():
    for item in movies_and_series_by_title:
        if isinstance(item, Series):
            print(f'{item.title} S{item.season:02d}E{item.episode:02d}')
#            print(f'{item.title} S{item.season:02d}E{item.episode:02d} ({item.year}) - {item.genre} ({item.views} views)')
            
def get_movies():
    for item in movies_and_series_by_title:
        if isinstance(item, Movies):
            print(f'{item.title} ({item.year})')
#            print(f'{item.title} ({item.year}) - {item.genre} ({item.views} views)')

    
print("----- BIBLIOTEKA FILMÓW -----")
print("     Filmy")
get_movies()
print("\n     Seriale")
get_series()
        