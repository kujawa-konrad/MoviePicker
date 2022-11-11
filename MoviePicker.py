# App for end user

from movie_func import MoviePicker

if __name__ == '__main__':
    dec = input("Hello! What do you want me to do?\nPick / Add / Exit\n")
    print(MoviePicker(dec))