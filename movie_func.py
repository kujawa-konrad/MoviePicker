# Func to search a db

from movie_methods import Movie
import random
import pandas as pd

# test_list will be changed to dataframe
# test_list = ['Inception', 'Pirates of th Caribbean', 'John Wick']

def MoviePicker(db):

    dec = input("Hello! What do you want me to do?\nPick / Add / Exit\n")

    while True:
        if dec == "Exit":
            return 'Bye!'
        elif dec == "Pick":
            # HAS TO BE CHANGED
            chosen = random.choice(db)
            return chosen
        elif dec == "Add":
            title = input('Enter the title of the movie\n')
            if title in db['Title']:
                return 'This movie is already in the database'
            else:
                lenght = input('Enter the lenght of the movie in minutes\n')
                genre = input('Enter the genre of the movie\n')
            new_movie = Movie(title, lenght, genre)

            # This does not update dataframe passed into the function
            new_row = {'Title':new_movie.title, 'Lenght':new_movie.length, 'Genre':new_movie.genre}
            db = db.append(new_row, ignore_index=True)
            return f"You've added a {new_movie.title} movie to your database"
        else:
            return 'Unknown command'

if __name__ == '__main__':
    data = {'Title':['Inception', 'Pirates of th Caribbean', 'John Wick'], 'Lenght':['Long', 'Long', 'Long'], 'Genre':['Thriller', 'Adventure', 'Action']}
    test_df = pd.DataFrame(data)

    print(MoviePicker(test_df))
    print(test_df)
