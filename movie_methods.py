# Class for every movie in db to choose from

import pandas as pd

class Movie:

    # Class will operate using pandas dataframe
    def assign_interval(self, length):
        length = str(length)
        if length.isnumeric() is False:
            raise ValueError("Error: Length must be defined using minutes")
        else:
            length = int(length)
            if length <= 80:
                interval = 'Short'
            elif length > 80 and length < 120:
                interval = 'Normal'
            else:
                interval = 'Long'
            return interval


    def __init__(self, title, length, genre):
        self.title = title
        self.length = self.assign_interval(length)
        self.genre = genre
        # add to db
        
    def __repr__(self):
        return self.title
    
    def change_title(self, title):
        self.title = title
    
    def change_length(self, length):
        self.length = self.assign_interval(length)
    
    def change_genre(self, genre):
        self.genre = genre

    def delete(self):
        # delete from db
        pass

if __name__ == '__main__':
    new_movie = Movie('John Wick', 101, 'action')
    print(new_movie)