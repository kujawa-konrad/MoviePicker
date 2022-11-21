# Func to search a db

from movie_methods import Movie
import pandas as pd


def MoviePicker(db):
    print('Hello!')

    while True:
        dec = input("What do you want me to do?\nPick / Add / Exit\n")

        if dec == "Exit":
            print('Bye!')
            break
        elif dec == "Pick":
            # Need to add option to search from every genre and every lenght
            lenght = input('Enter the lenght of the movie\nShort / Normal / Long\n')
            if lenght not in ['Short', 'Normal', 'Long']:
                print('Unknown lenght\n')
                continue
            genre = input('Enter the genre of the movie\n')
            if genre not in db['Genre'].unique():
                print('Unknown genre')
                continue

            chosen = db[(db['Lenght']==lenght)&(db['Genre']==genre)].sample()['Title'].item()
            print(f'Recommended movie is "{chosen}"')
            break
        elif dec == "Add":
            title = input('Enter the title of the movie\n')
            if (db['Title'].eq(title)).any():
                print('This movie is already in the database')
                continue
            else:
                lenght = input('Enter the lenght of the movie in minutes\n')
                genre = input('Enter the genre of the movie\n')
            try:
                new_movie = Movie(title, lenght, genre)
            except ValueError as e:
                print(e)
                continue

            new_row = pd.DataFrame([[new_movie.title, new_movie.length, new_movie.genre]], columns=['Title', 'Lenght', 'Genre'])
            db = pd.concat([db, new_row], ignore_index=True)
            print(f"You've added a {new_movie.title} movie to your database")
            return db
        else:
            print('Unknown command')

if __name__ == '__main__':
    data = {'Title':['Inception', 'Pirates of the Caribbean', 'John Wick'], 'Lenght':['Long', 'Long', 'Long'], 'Genre':['Thriller', 'Adventure', 'Action']}
    test_df = pd.DataFrame(data)
    db_check = MoviePicker(test_df)
    if db_check is not None:
        test_df = db_check
    else:
        pass
    print(test_df)
