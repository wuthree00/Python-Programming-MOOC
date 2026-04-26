## Please write a function named add_movie(database: list, name: str, director: str, year: int, runtime: int),
## which adds a new movie object into a movie database.

# The database is a list, and each movie object in the list is a dictionary.
# The dictionary should contain the following keys.
# - name
# - director
# - year
# - runtime

# The values attached to these keys are given as arguments to the function.
# An example of its use:


## Solution:
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    #database = [movie1, movie2, movie3, etc] each movie is a dictionary w keys name, director, year, runtime
    movie = {"name": name, "director": director, "year": year, "runtime": runtime}
    database.append(movie)

if __name__ == "__main__":
    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    print(database)


## The model solution provided:
# def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    # Python accepts splitting rows from punctuation
    # The addition becomes more readable when parts are divided into separate rows
#     movie = {"name": name,
#                "director": director,
#                "year": year,
#                "runtime": runtime}
 
#     database.append(movie)
