import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def generate_token(user):
    timestampe = datetime.utcnow() + timedelta(hours=2)
    dictionary_user = {"sub": user, "exp": timestampe}
    token = jwt.encode(dictionary_user, SECRET_KEY, algorithm="HS256")
    return token