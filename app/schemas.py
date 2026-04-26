from sqlalchemy import String, Integer, Column, ForeignKey, DateTime, func
from sqlalchemy.orm import declarative_base, relationships

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

##
# MODELO PARA A TABELA WORKOUTS_EXERCISES
class WorkoutsExercises(Base):
    __tablename__ = 'workouts_exercises'
    id = Column(Integer, primary_key=True)
    id_workout = Column(Integer, ForeignKey("workouts.id"), nullable=False)
    id_exercise = Column(Integer, ForeignKey("exercises.id"), nullable=False)

##
# MODELO PARA A TABELA SETS
class Sets(Base):
    __tablename__ = 'sets'
    id = Column(Integer, primary_key=True)
    id_workout_exercise = Column(Integer, ForeignKey("workouts_exercises.id"), nullable=False)
    weight = Column(Integer, nullable=False)
    reps = Column(Integer, nullable=False)
    

