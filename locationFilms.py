from enum import Enum

class Movie:
    def __init__(self, title, date, director, category):
        self.title = title
        self.date = date
        self.director = director
        self.category = category
    
    def display_movie_info(self):
        print(f"The movie {self.title} is a {self.category}, it came out on {self.date} and is realized by {self.director}.")

class Director:
    def __init__(self, lastname, firstname, birth_year):
        self.lastname = lastname
        self.firstname = firstname
        self.birth_year = birth_year

    def age(self):
        return 2025 - self.birth_year
    
class Category(Enum):
    Drame = 1
    Policier = 2

class Clients:
    def __init__(self, lastname, firstname, movie_list):
        self.lastname = lastname
        self.firstname = firstname
        self.movie_list = movie_list
    
    def add_movie(self, movie):
        self.movie_list.append(movie)



movie1 = Movie("Anatomie d’une chute", 2023, "Justine Triet", Category.Drame.name)
movie2 = Movie("Polisse", 2011, "Maïwenn", Category.Policier.name)
movie3 = Movie("Les filles du docteur March", 2019, "Greta Gerwig", Category.Drame.name)

director1 = Director("Triet", "Justine", 1978)
director2 = Director("Le Besco", "Maïwenn", 1976)
director3 = Director("Gerwig", "Greta", 1983)

client1 = Clients("Toto", "Tatou", [])

# Display movies infos
movie1.display_movie_info()
movie2.display_movie_info()
movie3.display_movie_info()

# Display age of the directors

print(f"Maïwenn est agée de {director2.age()} ans.")
print(f"Greta Gerwig est agée de {director3.age()} ans.")

# Add a film to the client's list
client1.add_movie(movie1)
client1.add_movie(movie2)

for movie in client1.movie_list: 
    print(movie.title)
