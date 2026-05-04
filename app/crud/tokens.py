from app.schemas import Tokens
from sqlalchemy.orm import Session

def add_token(db: Session, token: str):
    token_created = Tokens(token=token)
    db.add(token_created)
    db.commit()
    db.refresh(token_created)
    return token_created

def read_tokens(db: Session, token):
    return db.query(Tokens).where(Tokens.token == token).all()