from app.schemas import Users
from sqlalchemy.orm import Session


# ROTAS A REFATORAR
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
    
        
