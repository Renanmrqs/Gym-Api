import sqlite3

connect = sqlite3.connect('gym.db')


with open("views.sql", 'r') as f:
    views = f.read() 

connect.executescript(views)
connect.close()
print('views created')