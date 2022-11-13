# App for end user

from movie_func import MoviePicker
import pandas as pd

df = pd.DataFrame(columns=['Title', 'Lenght', 'Genre'])

if __name__ == '__main__':
    print(MoviePicker(df))