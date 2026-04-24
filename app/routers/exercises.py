from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud.exercises import get_exercises

router = APIRouter()

@router.get("/exercises")
def read_exercises(db: Session = Depends(get_db)):
    return get_exercises(db)
##
#TABELAS A REFATORAR
# @app.get("/exercises")
# def read_exercises():
#     return get_exercises()