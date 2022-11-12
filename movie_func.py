# Func to search a db

from movie_methods import Movie
import random

# test_list will be changed to dataframe
test_list = ['Inception', 'Pirates of th Caribbean', 'John Wick']

def MoviePicker(db):

    dec = input("Hello! What do you want me to do?\nPick / Add / Exit\n")

    while True:
        if dec == "Exit":
            return 'Bye!'
        elif dec == "Pick":
            chosen = random.choice(test_list)
            return chosen
        elif dec == "Add":
            name = input('Enter the name of the movie\n')
            if name in db:
                return 'This movie is already in the database'
            else:
                lenght = input('Enter the lenght of the movie in minutes\n')
                genre = input('Enter the genre of the movie\n')
            new_movie = Movie(name, lenght, genre)

            # Here new entry will be added to db using Pandas
            db.append(new_movie.name)
            return f"You've added a {new_movie.name} movie to your database"
        else:
            return 'Unknown command'

if __name__ == '__main__':
    print(MoviePicker(test_list))
    print(test_list)
