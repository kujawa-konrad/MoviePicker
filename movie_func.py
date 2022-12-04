# Func to search a db

from movie_methods import Movie
import pandas as pd
import sqlite3


def MoviePicker(sql_db):
    print('Hello!')

    conn = sqlite3.connect(sql_db) 
          
    sql_query = pd.read_sql_query ('''
                                SELECT
                                *
                                FROM To_watch
                                ''', conn)

    db = pd.DataFrame(sql_query, columns = ['Title', 'Length', 'Genre'])

    while True:
        dec = input("\nWhat do you want me to do?\nPick / Add / Exit\n\n")

        if dec == "Exit":
            print('\nBye!')
            break
        elif dec == "Pick":

            length = input('Enter the length of the movie\nShort / Normal / Long\n')
            if length not in ['Short', 'Normal', 'Long'] and length != '':
                print('Unknown length\n')
                continue

            genre = input('Enter the genre of the movie\n')
            if genre not in db['Genre'].unique() and genre != '':
                print('Unknown genre\n')
                continue
            
            try:
                if length == '' and genre == '':
                    chosen = db.sample()['Title'].item()
                elif length == '':
                    chosen = db[(db['Genre']==genre)].sample()['Title'].item()
                elif genre == '':
                    chosen = db[(db['Length']==length)].sample()['Title'].item()
                else:
                    chosen = db[(db['Length']==length)&(db['Genre']==genre)].sample()['Title'].item()
            except:
                print('There was no entries in database with given requirements\n')
                continue
                
            print(f'Recommended movie is "{chosen}"\n')


            while True:
                watch = input('Are you going to watch this? [Y / N]\n')
                if watch not in ['Y', 'N']:
                    print('Please select "Y" or "N"\n')
                    continue
                elif watch == 'Y':
                    new_df = pd.DataFrame(columns=db.columns)
                    rows = db.loc[db['Title']==chosen, :]

                    new_df = pd.concat([new_df, rows], ignore_index=True)
                    db.drop(rows.index, inplace=True)

                    new_df.to_sql('Watched', conn, if_exists='append', index=False)
                    db.to_sql('To_watch', conn, if_exists='replace', index=False)

                    break
                else:
                    break

        elif dec == "Add":
            title = input('Enter the title of the movie\n')

            if (db['Title'].eq(title)).any():
                print('\nThis movie is already in the database\n')
                continue
            else:
                length = input('Enter the length of the movie in minutes\n')
                genre = input('Enter the genre of the movie\n')
            try:
                new_movie = Movie(db, title, length, genre)
            except ValueError as e:
                print(e)
                continue

            print(f"You've added a {new_movie} movie to your database\n")
            new_movie.database.to_sql('To_watch', conn, if_exists='replace', index=False)

        else:
            print('Unknown command\n')
