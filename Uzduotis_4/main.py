# Sukurkite filmų klasę "Movie", kuri:
# * Turės klasės lygio 'docstring' tipo komentarą, trumpai aprašantį, kas tai
#   per klasė.
# * Turės 'docstring' tipo komentarą prie kiekvieno metodo, trumpai aprašantį,
#   ką tas metodas atlieka.
# * Gebės sukurti objektus su 3 savybėmis ir 1 metodu.

# Naudojant šią klasę sukurkite bent du skirtingus filmų objektus.

# Savybės:
# * title (str)
# * director (str)
# * budget (int)

# Metodas:
# * was_expensive() - jeigu filmo "budget" yra daugiau nei 100 mln. USD,
#   grąžins True, kitu atveju - False.

import math

class Movie:
    """Apibūdina filmą trimis savybėmis - pavadinimu, režisieriumi, biudžeto dydžiu."""
    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget
        
    def was_expensive(self):
        """Grąžina boolean, kuris nurodo ar filmo biudžetas buvo brangus."""
        return self.budget > math.pow(10, 6)
    
movie_a = Movie("Movie A", "Director A", 10000)
movie_b = Movie("Movie B", "Director B", 100000)
movie_c= Movie("Movie C", "Director C", 100000000)

print(movie_a.was_expensive())
print(movie_b.was_expensive())
print(movie_c.was_expensive())