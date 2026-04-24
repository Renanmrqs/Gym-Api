from fastapi import FastAPI
# , exceptions, HTTPException, security, Depends
from app.routers import exercises, users
# 


app = FastAPI()

app.include_router(exercises.router)
app.include_router(users.router)


# READS
# cria a rota padrao
@app.get("/health")
def health():
    return {"status": "ok"}

#cria a rota de puxar o exercicio








