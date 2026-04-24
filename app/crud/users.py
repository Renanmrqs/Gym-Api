from app.models import Exercise, Users
from sqlalchemy.orm import Session
from sqlalchemy import select


# ROTAS A REFATORAR
# PEGAR TODOS USERS
# def get_users():
#     conn = get_connection()
#     cur = conn.cursor(cursor_factory=RealDictCursor)
    
#     cur.execute('SELECT * FROM "users"') 
#     rows = cur.fetchall()
#     return rows
def get_exercises_id(id, db: Session):
    user = db.query(Exercise).filter(Exercise.id == id).first()
    return user

def get_users_by_name(name, db: Session):
    user = db.query(Users).filter(Users.name == name).first()
    return user

# # busca usuario especifico atraves do nome
# def get_users_by_name(name):
#     conn = get_connection()
#     cur = conn.cursor(cursor_factory=RealDictCursor)
#     cur.execute(""" 
#     SELECT * FROM "users"
#     WHERE name = %s  
#     """, (name,)) 
#     row = cur.fetchone()
#     return row


# adiciona um user na tabela user
# def create_register(name, password):
#     conn = get_connection()
#     try:
#         cur = conn.cursor()
#         cur.execute("""
#         INSERT INTO "users" ("name", "password")
#         VALUES
#         (%s, %s);
#         """, (name, password))
#         conn.commit()
#     finally:
#         conn.close()