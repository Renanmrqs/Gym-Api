from app.schemas import Exercise
from sqlalchemy.orm import Session
from sqlalchemy import select, insert
## TABELAS A FAZER EXERCISES

## puxa todos os exercicios
def get_exercises(db: Session):
    return db.query(Exercise).all()

# puxa os exercicios por id  
def get_exercises_id(id, db: Session):
    user = db.query(Exercise).where(Exercise.id == id).all()
    return user

# cria os exercicios (método post)
def create_exercises(db: Session, name: str):
    exercise = Exercise(name=name)
    db.add(exercise)
    db.commit()
    db.refresh(exercise)
    return exercise

