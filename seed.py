import sqlite3

connect = sqlite3.connect('gym.db')


with open("seed.sql", 'r') as f:
    seed = f.read() 

connect.executescript(seed)
connect.close()
print('adicioned')