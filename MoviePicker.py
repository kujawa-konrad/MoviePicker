# App for end user

from movie_func import MoviePicker
import pandas as pd

new_row = pd.Series()
df = pd.DataFrame()
df = df.append(new_row, ignore_index=True)

if __name__ == '__main__':
    print(MoviePicker(df))