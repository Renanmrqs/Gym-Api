import sqlite3
from app.auth import pwd_context
from app.database import get_connection

connect = sqlite3.connect('gym.db')


with open("seed.sql", 'r') as f:
    seed = f.read() 

connect.executescript(seed)
connect.close()

### migrando login dos users
def migrate_users():
    conn = get_connection()
    cur = conn.cursor()
    
    users = cur.execute("""
        SELECT * FROM "users";
        """)
    rows = cur.fetchall()
    users = [dict(row) for row in rows]
    print(users)
    for user in users:
        senha_atual = pwd_context.hash(user["password"])
        cur.execute("""
        UPDATE "users" SET password = ? 
        WHERE id = ?;            
        """, (senha_atual, user["id"]))
    conn.commit()
    conn.close()
    print('ok')

migrate_users()

print('adicioned')