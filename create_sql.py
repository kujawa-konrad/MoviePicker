import sqlite3

conn = sqlite3.connect('test_database') 
cur = conn.cursor()

# It would be a cleaner solution to create 2 tables (To_watch and Watched) instead adding Y/N mark everytime

cur.execute('''
          CREATE TABLE IF NOT EXISTS To_watch
          ([Title] TEXT PRIMARY KEY, [Length] TEXT, [Genre] TEXT)
          ''')

# cur.execute('''
#           CREATE TABLE IF NOT EXISTS Watched
#           ([Title] TEXT PRIMARY KEY, [Length] TEXT, [Genre] TEXT)
#           ''')

          
cur.execute('''
          INSERT INTO To_watch (Title, Length, Genre)

                VALUES
                ('Inception', 'Long', 'Thriller'),
                ('Werewolf by Night', 'Short', 'Action'),
                ('Pirates of the Caribbean', 'Long', 'Adventure'),
                ('John Wick', 'Normal', 'Action')
          ''')                     

conn.commit()