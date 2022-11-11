# Class for every movie in db to choose from
# It would be nice to create lenght ranges for self.length based on given time in minutes

class Movie:
    def __init__(self, length, genre):
        self.length = length
        self.genre = genre
        # add to db
    
    def change_length(self, length):
        self.length = length
    
    def change_genre(self, genre):
        self.genre = genre

    def delete(self):
        # delete from db
        pass