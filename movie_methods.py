# Class for every movie in db to choose from

import pandas as pd

class Movie:

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

    def __init__(self, database, title, length, genre):
        self.title = title
        self.length = self.assign_interval(length)
        self.genre = genre
        self.database = database

        new_row = pd.DataFrame([[self.title, self.length, self.genre]], columns=['Title', 'Length', 'Genre'])
        self.database = pd.concat([self.database, new_row], ignore_index=True)
        
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
