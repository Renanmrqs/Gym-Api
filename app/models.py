from sqlalchemy import String, Integer, Column, ForeignKey, DateTime, func
from sqlalchemy.orm import declarative_base

# MODELO BASE USANDO ORM E SQLALCHEMY
Base = declarative_base()
##
# MODELO PARA TABELA EXERCISE
class Exercise(Base):
    __tablename__ = "exercises"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

##
# MODELO PARA TABELA USERS
class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False) 

##
# MODELO PARA A TABELA WORKOUTS
class Workouts(Base):
    __tablename__ = 'workouts'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey("users.id"), nullable=False)
    datetime = Column(DateTime(), server_default=func.now())




############CLASSES ANTIGAS ABAIXO
# base: o que é comum em todos os casos DB EXERCISES
# class ExerciseBase(BaseModel):
#     name: str

# # criação: só o que o usuário manda (herda do base)
# class ExerciseCreate(ExerciseBase):
#     pass

# # resposta: inclui o id que o banco gerou (herda do base)
# class Exercise(ExerciseBase):
#     id: int

# DB USERS

# class UsersBase(BaseModel):
#     name: str
#     password: str
# class UsersCreate(UsersBase):
#     pass

# class Users(UsersBase):
#     id: int


# class LoginRequest(BaseModel):
#     name: str
#     password: str

# # DB WORKOUTS

# class WorkoutsBase(BaseModel):
#     id_user: int
    
    
# class WorkoutCreate(WorkoutsBase):
#     pass

# class Workout(WorkoutsBase):
#     id: int
    
# # DB WORKOUTS_EXERCISES

# class WorkoutsExercisesBase(BaseModel):
#     id_workout: int
#     id_exercise: int
    
# class WorkoutsExercisesCreate(WorkoutsExercisesBase):
#     pass

# class WorkoutsExercises(WorkoutsExercisesBase):
#     id: int
    
# # DB SETS

# class SetsBase(BaseModel):
#     weight: float
#     reps: int
#     id_workout_exercise: int
    
# class SetsCreate(SetsBase):
#     pass

# class Sets(SetsBase):
#     id: int