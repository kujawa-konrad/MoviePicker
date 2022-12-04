import sqlite3

conn = sqlite3.connect('test_database') 
cur = conn.cursor()

# Script that resets SQL database to ease development

cur.execute('''
          DROP TABLE IF EXISTS To_watch
          ''')

cur.execute('''
          DROP TABLE IF EXISTS Watched
          ''')

cur.execute('''
          CREATE TABLE IF NOT EXISTS To_watch
          ([Title] TEXT PRIMARY KEY, [Length] TEXT, [Genre] TEXT)
          ''')

cur.execute('''
          CREATE TABLE IF NOT EXISTS Watched
          ([Title] TEXT PRIMARY KEY, [Length] TEXT, [Genre] TEXT)
          ''')

          
cur.execute('''
          INSERT OR IGNORE INTO To_watch (Title, Length, Genre)

                VALUES
                ('Inception', 'Long', 'Thriller'),
                ('Werewolf by Night', 'Short', 'Action'),
                ('Pirates of the Caribbean', 'Long', 'Adventure'),
                ('John Wick', 'Normal', 'Action'),
                ('David Attenborough: A Life On Our Planet', 'Normal', 'Documentary'),
                ('Avengers: Endgame', 'Long', 'Action')
          ''')                     

conn.commit()