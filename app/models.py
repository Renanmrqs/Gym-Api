from pydantic import BaseModel



##
# modelo de registrar usuario

class RegisterRequest(BaseModel):
    name: str
    password: str


