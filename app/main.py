import sqlite3
from fastapi import FastAPI, exceptions
from app.crud import get_exercises, create_exercise, get_workout_detail, get_exercises_id, get_workouts_by_user, create_workout, create_workout_exercise, create_set, get_historic, get_users
from app.models import ExerciseCreate, WorkoutsExercisesCreate, WorkoutCreate, SetsCreate

app = FastAPI()

# READS
# cria a rota padrao
@app.get("/health")
def health():
    return {"status": "ok"}

#cria a rota de puxar o exercicio
@app.get("/exercises")
def read_exercises():
    return get_exercises()

# cria a rota de puxar exercicio por id
@app.get("/exercises/{id}")
def read_exercises_detail(id: int):
    return get_exercises_id(id)


# cria a rota de puxa o treino de acordo com o id de treino 
@app.get("/workout_detail_w_workout/{id_workout}")
def read_workout_detail_workout(id_workout: int):
    return get_workout_detail(id_workout)

# cria a rota de puxa o treino de acordo com o id do user
@app.get("/workout_detail_w_user/{id_user}")
def read_workout_detail_user(id_user: int):
    return get_workouts_by_user(id_user)


# faz a rota de puxar o historico de sets completo com o nome
@app.get("/history/{name_user}")
def read_history_sets_by_user(name_user: str):
    result = get_historic(name_user)
    if not result:
        raise exceptions.HTTPException(status_code=400, detail=f'{name_user} not in table')
    return result

# faz a rota de puxar tudo da tabela usuarios 
@app.get("/users")
def read_users():
    return get_users()

# CREATES

# faz a rota de adicionar exercicio na tabela exercicios
@app.post("/exercises")
def post_exercise(exercise: ExerciseCreate):
    try:
        create_exercise(exercise.name)
        return {"message": f"exercise {exercise.name} Created"}
    except sqlite3.IntegrityError:
        raise exceptions.HTTPException(status_code=400, detail=f"{exercise.name} already in the table")

# faz a rota de criar treino 
@app.post("/workout")
def post_workout(workout: WorkoutCreate):
    try:
        create_workout(workout.id_user)
        return {"message": "Workout Created", "id": workout.id_user}
    except sqlite3.IntegrityError:
        raise exceptions.HTTPException(status_code=400, detail=f'{workout.id_user} not in the table')
    

# faz a rota de adicionar exercicio no treino
@app.post("/workout_exercise")
def post_add_exercise_in_workout(workout_exercise: WorkoutsExercisesCreate):
    try:
        id = create_workout_exercise(workout_exercise.id_workout, workout_exercise.id_exercise)
        return {"message": f"Exercise add in workout", "id": id}
    except sqlite3.IntegrityError:
        raise exceptions.HTTPException(status_code=400, detail=f'Workout or Exercise ID not found, or already added.')

# faz a rota de registrar a série
@app.post("/sets")
def post_sets(sets: SetsCreate):
    try:
        create_set(sets.id_workout_exercise, sets.weight, sets.reps)
        return {"message": f"Exercise add weight: {sets.weight} | reps: {sets.reps}"}
    except sqlite3.IntegrityError:
        raise exceptions.HTTPException(status_code=400, detail=f'{sets.id_workout_exercise} not in the table')