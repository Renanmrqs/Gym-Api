from fastapi import APIRouter, Depends, HTTPException, security, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth import pwd_context, generate_token, verify_token
from app.crud.users import get_users_by_name, get_users, create_register
from sqlalchemy.exc import IntegrityError
from app.models import RegisterRequest

# verificações de login
router = APIRouter()
security_rote = security.OAuth2PasswordBearer(tokenUrl="login")
def get_current_user(token: str = Depends(security_rote)):
    user  = verify_token(token)
    return user

###
# rota de puxar todos os usuarios
@router.get("/users")
def read_all_users(db: Session = Depends(get_db)):
    return get_users(db)


# #####registro de usuario
# ##faz a rota de criar o registro    
@router.post("/register")
def post_register(register: RegisterRequest, db: Session = Depends(get_db)):
    try:
        password_criptografed = pwd_context.hash(register.password)

        create_register(db, register.name, password_criptografed)
        
        return {"message": f"user {register.name} registred"}
    except IntegrityError:
        raise HTTPException(status_code=400, detail=f'{register.name} already in table')






# faz rota do usuario logar na aplicacao
@router.post("/login")
def post_login(form_data: security.OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    login_return = get_users_by_name(form_data.username, db)
    if not login_return:
        raise HTTPException(status_code=400, detail=f'{form_data.username} is not registred')
    
    password_corrrect = pwd_context.verify(form_data.password, login_return.password)
    if password_corrrect == False:
        raise HTTPException(status_code=400, detail=f'incorrect password, try again.')
    
    token = generate_token(form_data.username)
    
    return {"access_token": token, "token_type": "bearer", "user_id": login_return.id}


#