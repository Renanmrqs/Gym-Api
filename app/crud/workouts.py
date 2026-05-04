from app.schemas import Workouts, WorkoutsExercises, Sets
from sqlalchemy.orm import Session
from sqlalchemy import text


# # buscar o historico pelo nome do usuario

def get_historic(db: Session, name_user: str):
    result = db.execute(
        text('SELECT * FROM workout_summary WHERE "user" = :name'),
        {"name": name_user}
    )
    return result.mappings().all()


# # busca treinos filtrando por usuario ID
def get_workouts_by_user(db: Session, user_id):
    return db.query(Workouts).filter(Workouts.id_user == user_id).all()
    

# # busca exercicio filtrando por id de treino

def get_workout_detail_by_workout(db: Session, workout_id):
    return db.query(WorkoutsExercises).filter(WorkoutsExercises.id_workout == workout_id).all()


# #CREATES:

#cria um dia de treino 
def create_workout(db: Session, user_id):
    result = Workouts(id_user=user_id)
    db.add(result)
    db.commit()
    db.refresh(result)
    return result

#adiciona um exercicio em um dia de treino 
def create_workout_exercise(db: Session, workout_id, exercise_id):
    result = WorkoutsExercises(id_workout=workout_id, id_exercise=exercise_id)
    db.add(result)
    db.commit()
    db.refresh(result)
    return result

# # adiciona na tabela sets 
def create_set(db: Session, workout_exercise_id, weight, reps):
    result = Sets(id_workout_exercise=workout_exercise_id, weight=weight, reps=reps)
    db.add(result)
    db.commit()
    db.refresh(result)
    return result


    