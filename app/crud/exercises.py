from app.models import Exercise
from sqlalchemy.orm import Session
from sqlalchemy import select, insert
## TABELAS A FAZER EXERCISES

def get_exercises(db: Session):
    return db.query(Exercise).all()
    
def get_exercises_id(id, db: Session):
    user = db.query(Exercise).where(Exercise.id == id).all()
    return user

# ###
# ###
def create_exercises(db: Session, name: str):
    exercise = Exercise(name=name)
    db.add(exercise)
    db.commit()
    db.refresh(exercise)
    return exercise
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
