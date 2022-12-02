# Func to search a db

from movie_methods import Movie
import pandas as pd


def MoviePicker(db):
    print('Hello!')

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
            
            # try:
            #     if length == '' and genre == '':
            #         chosen = db[(db['Watched']=='N')].sample()['Title'].item()
            #     elif length == '':
            #         chosen = db[(db['Genre']==genre)&(db['Watched']=='N')].sample()['Title'].item()
            #     elif genre == '':
            #         chosen = db[(db['Length']==length)&(db['Watched']=='N')].sample()['Title'].item()
            #     else:
            #         chosen = db[(db['Length']==length)&(db['Genre']==genre)&(db['Watched']=='N')].sample()['Title'].item()
            # except:
            #     print('There was no entries in database with given requirements\n')
            #     continue
            
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

            # The part below will be replaced by second table in SQL database
            
            # if 'Y' ->  rows = ...       new_df = ...       conn = ...
            # new_df = new_df.append(rows, ignore_index=True)
            # db.drop(rows.index, inplace=True)
            # new_df.to_sql('Watched', conn, if_exists='append')

            # while True:
            #     watch = input('Are you going to watch this? [Y / N]\n')
            #     if watch not in ['Y', 'N']:
            #         print('Please select "Y" or "N"\n')
            #         continue
            #     elif watch == 'Y':
            #         db.loc[db['Title']==chosen, 'Watched'] = watch
            #         break
            #     else:
            #         break

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

            print(f"You've added a {new_movie.title} movie to your database\n")
            return new_movie.database
        else:
            print('Unknown command\n')

if __name__ == '__main__':
    data = {'Title':['Inception', 'Werewolf by Night', 'Pirates of the Caribbean', 'John Wick'], 'Length':['Long', 'Short', 'Long', 'Normal'], 'Genre':['Thriller', 'Action', 'Adventure', 'Action'], 'Watched':['N', 'N', 'N', 'N']}
    test_df = pd.DataFrame(data)
    db_check = MoviePicker(test_df)
    if db_check is not None:
        test_df = db_check
    else:
        pass
    print(test_df)
