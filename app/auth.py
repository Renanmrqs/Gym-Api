import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
import os
from dotenv import load_dotenv
from fastapi import HTTPException

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def generate_token(user):
    timestampe = datetime.utcnow() + timedelta(hours=2)
    dictionary_user = {"sub": user, "exp": timestampe}
    token = jwt.encode(dictionary_user, SECRET_KEY, algorithm="HS256")
    return token

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    
        user = payload.get("sub")
        if user is None: 
            raise HTTPException(status_code=401, detail="Invalid token")
        return user
    
    except jwt.DecodeError:
        raise HTTPException(status_code=401, detail=f"O token enviado está num formato inválido.")
    
    
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Expired time.")
    
    except jwt.PyJWKError:
        raise HTTPException(status_code=401, detail="Invalid user.")