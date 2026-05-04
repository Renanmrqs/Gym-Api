from fastapi import APIRouter, Depends, HTTPException
from app.models import RegisterToken
from app.crud.tokens import add_token, read_tokens
from sqlalchemy.orm import Session
from app.database import get_db
from sqlalchemy.exc import IntegrityError
from app.routers.users import get_current_token, get_current_user

router = APIRouter()


@router.post(f'/logout')
def post_logout(token: str = Depends(get_current_token), user: str = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        tk = add_token(db, token)
        return {'message': 'token adicioned', 'data': tk}
    except IntegrityError:
        raise HTTPException(status_code=400, detail=f'token already in table')
    