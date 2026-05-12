from app.schemas import Users
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


# PEGAR TODOS USERS
def get_users(db: Session):
    return db.query(Users).all()



# busca user pelo nome
def get_users_by_name(name, db: Session):
    user = db.query(Users).filter(Users.name == name).first()
    return user


# adiciona um user na tabela user
def create_register(db: Session, name, password):
    user = Users(name=name, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user