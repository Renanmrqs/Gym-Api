from sqlalchemy import String, Integer, Column, ForeignKey, DateTime, func, BigInteger, Text, TIMESTAMP
from sqlalchemy.orm import declarative_base, relationships
from datetime import datetime, timezone, timedelta
import zoneinfo

#funcao para pegar o fuso horario atual de sao paulo
fuso_br = timezone(timedelta(hours=-3))
def actual_hour():
    return datetime.now(fuso_br)

# MODELO BASE USANDO ORM E SQLALCHEMY
Base = declarative_base()
##
# MODELO PARA TABELA EXERCISE
class Exercise(Base):
    __tablename__ = "exercises"
    id = Column(BigInteger, primary_key=True)
    name = Column(Text, nullable=False)

##
# MODELO PARA TABELA USERS
class Users(Base):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    name = Column(Text, nullable=False, unique=True)
    password = Column(Text, nullable=False) 

##
# MODELO PARA A TABELA WORKOUTS
class Workouts(Base):
    __tablename__ = 'workouts'
    id = Column(BigInteger, primary_key=True)
    id_user = Column(BigInteger, ForeignKey("users.id"), nullable=False)
    datetime = Column(DateTime(timezone=True), default=actual_hour)

##
# MODELO PARA A TABELA WORKOUTS_EXERCISES
class WorkoutsExercises(Base):
    __tablename__ = 'workouts_exercises'
    id = Column(BigInteger, primary_key=True)
    id_workout = Column(BigInteger, ForeignKey("workouts.id"), nullable=False)
    id_exercise = Column(BigInteger, ForeignKey("exercises.id"), nullable=False)

##
# MODELO PARA A TABELA SETS
class Sets(Base):
    __tablename__ = 'sets'
    id = Column(BigInteger, primary_key=True)
    id_workout_exercise = Column(BigInteger, ForeignKey("workouts_exercises.id"), nullable=False)
    weight = Column(Integer, nullable=False)
    reps = Column(Integer, nullable=False)
    

