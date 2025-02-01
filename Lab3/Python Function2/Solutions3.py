# Movie tasks
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
    ]

# Task 1: Check if a movie's IMDB score is above 5.5
def is_high_score(movie):
    return movie["imdb"] > 5.5

    print(is_high_score(movies[0]))

# Task 2: Sublist of movies with IMDB > 5.5
def high_score_movies(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]

    print(high_score_movies(movies))

# Task 3: Movies by category
def movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]

    print(movies_by_category(movies, "Romance"))

# Task 4: Average IMDB score of movies
def average_imdb(movies):
    return sum(movie["imdb"] for movie in movies) / len(movies)

    print(average_imdb(movies))

# Task 5: Average IMDB score by category
def average_imdb_by_category(movies, category):
    filtered_movies = movies_by_category(movies, category)
    return average_imdb(filtered_movies) if filtered_movies else 0

    print(average_imdb_by_category(movies, "Romance"))
