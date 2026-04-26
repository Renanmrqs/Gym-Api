from fastapi import FastAPI
from app.routers import exercises, users, workouts

app = FastAPI()

app.include_router(exercises.router)
app.include_router(users.router)
app.include_router(workouts.router)


@app.get("/health")
def health():
    return {"status": "ok"}










