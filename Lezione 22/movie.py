class Movie:

    def __init__(self, movie_id:str, title:str, director:str, is_rented:bool):

        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = is_rented

    def rent(self) -> bool:

        if self.movie_id is self.is_rented:
            self.is_rented == True
        else:
            raise Exception (f"Il film '{self.title}' è già noleggiato")

    def return_movie(self) -> bool:

        if self.movie_id is not self.is_rented:
            self.is_rented == False
        else:
            raise Exception (f"Il film '{self.title}' non è stato noleggiato da questo cliente")   


class Customer:

    def __init__(self, customer_id: str, name: str, rented_movies: list[Movie]):

        self.customer_id = customer_id
        self.name = name
        self.rented_movies = rented_movies

    def rent_movie(self, movie: Movie):

        if movie.is_rented == True:
            self.rented_movies.append(movie.movie_id)
        else:
            raise Exception (f"Il film '{movie.title}' è già noleggiato")

    def return_movie(self, movie: Movie):

        if movie.movie_id in self.rented_movies:
            self.rented_movies.remove(movie.movie_id)
        else:
            raise Exception (f"Il film '{movie.title}' non è stato noleggiato da questo cliente")


class VideoRentalStore:

    def __init__(self, movies: dict[str, Movie], customers: dict[str, Customer]):

        self.movies = movies
        self.customers = customers

    def add_movie(self, movie_id: str, title: str, director: str):

        if movie_id in self.movies:
            raise Exception ("Il film con ID '{movie_id}' esiste già")
        else:
            movie_2 = Movie (movie_id, title, director, False)
            self.movies[movie_id] = movie_2
            return movie_2

    def register_customer(self, customer_id: str, name: str):

        if customer_id in self.customers:
            raise Exception (f"Il cliente con ID '{customer_id}' è già registrato")     
        else:
            customer2_id = Customer(customer_id, name)
            self.customers[customer_id] = customer2_id   
            return customer2_id
        
    def rent_movie(self, customer_id: str, movie_id: str):

        if movie_id and customer_id in self.movies and self.customers:
            self.customers[customer_id].rent_movie (self.movies[movie_id])
        else:
            raise Exception ("Cliente o Film non trovato")

    def return_movie(self, customer_id: str, movie_id: str):

        if movie_id and customer_id in self.movies and self.customers:  
            self.customers[customer_id].return_movie (self.movies[movie_id])    
        else:
            raise Exception ("Cliente o FIlm non trovato")
        
    def get_rented_movies(self, customer_id: str) -> list[Movie]:

        if customer_id in self.customers:
            return self.customers[customer_id].rented_movies
        else:
            raise Exception ("Cliente non trovato")
            