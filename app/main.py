from fastapi import FastAPI
from app.routers import exercises, users, workouts, tokens

app = FastAPI()

app.include_router(exercises.router)
app.include_router(users.router)
app.include_router(workouts.router)
app.include_router(tokens.router)

@app.get("/health")
def health():
    return {"status": "ok"}










