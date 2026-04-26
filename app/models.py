from pydantic import BaseModel



##
# modelo de registrar usuario

class RegisterRequest(BaseModel):
    name: str
    password: str

## modelo de registrar exercicios

class WorkoutsBase(BaseModel):
    id_user: int
    
    
class WorkoutCreate(WorkoutsBase):
    pass

class Workout(WorkoutsBase):
    id: int
    
# DB WORKOUTS_EXERCISES

class WorkoutsExercisesBase(BaseModel):
    id_workout: int
    id_exercise: int
    
class WorkoutsExercisesCreate(WorkoutsExercisesBase):
    pass

class WorkoutsExercises(WorkoutsExercisesBase):
    id: int

# DB SETS

class SetsBase(BaseModel):
    weight: float
    reps: int
    id_workout_exercise: int
    
class SetsCreate(SetsBase):
    pass

class Sets(SetsBase):
    id: int