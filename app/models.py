from pydantic import BaseModel

# base: o que é comum em todos os casos DB EXERCISES
class ExerciseBase(BaseModel):
    name: str

# criação: só o que o usuário manda (herda do base)
class ExerciseCreate(ExerciseBase):
    pass

# resposta: inclui o id que o banco gerou (herda do base)
class Exercise(ExerciseBase):
    id: int

# DB USERS

class UsersBase(BaseModel):
    name: str
    
class UsersCreate(UsersBase):
    pass

class Users(UsersBase):
    id: int

# DB WORKOUTS

class WorkoutsBase(BaseModel):
    id_user: int
    datetime: str
    
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