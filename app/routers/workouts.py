from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud.workouts import get_historic, get_workouts_by_user, get_workout_detail_by_workout, create_workout, create_workout_exercise, create_set
from sqlalchemy.exc import IntegrityError
from app.routers.users import get_current_user
from app.models import WorkoutCreate, WorkoutsExercisesCreate, SetsCreate

router = APIRouter()

# # cria a rota de puxa o treino de acordo com o id de treino 
@router.get("/workout_detail_w_workout/{id_workout}")
def read_workout_detail_workout(id_workout: int, user: str = Depends(get_current_user), db: Session = Depends(get_db)):
    return get_workout_detail_by_workout(db, id_workout)


# # cria a rota de puxa o treino de acordo com o id do user
@router.get("/workout_detail_w_user/{id_user}")
def read_workout_detail_user(id_user: int, user: str = Depends(get_current_user), db: Session = Depends(get_db)):
    return get_workouts_by_user(db, id_user)


# # faz a rota de puxar o historico de sets completo com o nome
@router.get("/history/{name_user}")
def read_history_sets_by_user(name_user: str, user: str = Depends(get_current_user), db: Session = Depends(get_db)):
    result = get_historic(db, name_user)
    if not result:
        raise HTTPException(status_code=400, detail=f'{name_user} not in table')
    return result


# # CREATES
# # faz a rota de criar treino 
@router.post("/workout")
def post_workout(workout: WorkoutCreate, user: str = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        workout_id = create_workout(db, workout.id_user)
        return {"message": "Workout Created", "data": workout_id}
    except IntegrityError:
        raise HTTPException(status_code=400, detail=f'{workout.id_user} not in the table')





# # faz a rota de adicionar exercicio no treino
@router.post("/workout_exercise")
def post_add_exercise_in_workout(workout_exercise: WorkoutsExercisesCreate, user: str = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        workout_exercise_id = create_workout_exercise(db, workout_exercise.id_workout, workout_exercise.id_exercise)
        return {"message": "Exercise added in workout", "data": workout_exercise_id}
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Workout or Exercise ID not found, or already added.")




# # faz a rota de registrar a série
@router.post("/sets")
def post_sets(sets: SetsCreate, user: str = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        create_set(db, sets.id_workout_exercise, sets.weight, sets.reps)
        return {"message": f"Exercise add weight: {sets.weight} | reps: {sets.reps}"}
    except IntegrityError:
        raise HTTPException(status_code=400, detail=f'{sets.id_workout_exercise} not in the table')

