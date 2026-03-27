import sqlite3

connect = sqlite3.connect('gym.db')

with open("schema.sql", 'r') as f:
    schema = f.read() 

connect.executescript(schema)
connect.close()
print('created')