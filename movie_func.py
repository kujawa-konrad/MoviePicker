# Func to search a db

from movie_methods import Movie

def MoviePicker(dec):

    while True:
        if dec == "Exit":
            return 'Bye!'
        elif dec == "Pick":
            break
        elif dec == "Add":
            break
        else:
            return 'Unknown command'
