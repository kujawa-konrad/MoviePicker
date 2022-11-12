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

            break
        else:
            return 'Unknown command'

if __name__ == '__main__':
    print(MoviePicker(test_list))
