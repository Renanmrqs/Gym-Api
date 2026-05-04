from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud.exercises import get_exercises, get_exercises_id, create_exercises
from sqlalchemy.exc import IntegrityError
from app.routers.users import get_current_user


router = APIRouter()

@router.get("/exercises")
def read_exercises(db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    return get_exercises(db)


# buscando exercicio pelo id
@router.get("/exercises/{id}")
def read_exercises_detail(id: int, user: str = Depends(get_current_user), db: Session = Depends(get_db)):
    return get_exercises_id(id, db)


# faz a rota de adicionar exercicio na tabela exercicios
@router.post("/exercises")
def post_exercise(exercise: str, user: str = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        create_exercises(db, exercise)
        return {"message": f"exercise {exercise} Created by {user}"}
    except IntegrityError:
        raise HTTPException(status_code=400, detail=f"{exercise} already in the table")