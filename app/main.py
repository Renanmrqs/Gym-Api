from fastapi import FastAPI
from app.routers import exercises, auth, workouts
from app.ws import websocket

app = FastAPI()

app.include_router(exercises.router)
app.include_router(auth.router)
app.include_router(workouts.router)
app.include_router(websocket.router)

@app.get("/health", tags=['health'])
def health():
    return {"status": "ok"}










