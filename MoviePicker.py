# App for end user

from movie_func import MoviePicker
import pandas as pd

# Database used in app will be based on SQL and will be updated every time
df = pd.DataFrame(columns=['Title', 'Lenght', 'Genre'])

if __name__ == '__main__':
    print(MoviePicker(df))