from app.models import Exercise
from sqlalchemy.orm import Session
## TABELAS A FAZER EXERCISES

def get_exercises(db: Session):
    return db.query(Exercise).all()
    


# ###
# def get_exercises():
#     conn = get_connection()
#     cur = conn.cursor(cursor_factory=RealDictCursor)
#     cur.execute("""
#     SELECT * FROM "exercises" 
#     """)
#     rows = cur.fetchall()
#     return rows

# ###
# def get_exercises_id(id):
#     conn = get_connection()
#     cur = conn.cursor(cursor_factory=RealDictCursor)
#     cur.execute("""
#     SELECT "name" FROM "exercises" 
#     WHERE id = %s
#     """, (id,))
#     rows = cur.fetchall()
#     return rows

# ###
# def create_exercise(name):
#     conn = get_connection()
#     try:
#         cur = conn.cursor()
#         cur.execute("""
#         INSERT INTO "exercises" ("name")
#         VALUES
#         (%s);
#         """, (name,))
#         conn.commit()
#     finally:
#         conn.close()
        
# ###
