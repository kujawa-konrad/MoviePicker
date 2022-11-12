# Class for every movie in db to choose from
# It would be nice to create lenght ranges for self.length based on given time in minutes

import pandas as pd

class Movie:

    df = pd.DataFrame()

    def __init__(self, name, length, genre):
        self.name = name
        self.length = length
        self.genre = genre
        # add to db
    def __repr__(self):
        return self.name
    
    def change_length(self, length):
        self.length = length
    
    def change_genre(self, genre):
        self.genre = genre

    def delete(self):
        # delete from db
        pass

if __name__ == '__main__':
    new_movie = Movie('John Wick', 'long', 'action')
    print(new_movie)