import sqlite3
import pandas as pd

conn = sqlite3.connect('test_database') 
          
sql_query = pd.read_sql_query ('''
                               SELECT
                               *
                               FROM To_watch
                               ''', conn)

df = pd.DataFrame(sql_query, columns = ['Title', 'Length', 'Genre'])

print(df)

# new_row = pd.DataFrame([['Love Story', 'Normal', 'Romance']], columns=['Title', 'Length', 'Genre'])
# df = pd.concat([df, new_row], ignore_index=True)

