# App for end user

from movie_func import MoviePicker
import pandas as pd
import sqlite3

# App will use SQL database and will pass a Pandas dataframe to the function

if __name__ == '__main__':
    conn = sqlite3.connect('test_database') 
          
    sql_query = pd.read_sql_query ('''
                                SELECT
                                *
                                FROM To_watch
                                ''', conn)

    df = pd.DataFrame(sql_query, columns = ['Title', 'Length', 'Genre'])
    # print(df)
    print(MoviePicker(df))