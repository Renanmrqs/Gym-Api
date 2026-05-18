from fastapi import FastAPI
from app.routers import exercises, auth, workouts
from app.ws import websocket
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://gym-api-08pc.onrender.com/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],            # Allows specific origins         
    allow_methods=["*"],              # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],              # Allows all headers
)


app.include_router(exercises.router)
app.include_router(auth.router)
app.include_router(workouts.router)
app.include_router(websocket.router)

@app.get("/health", tags=['health'])
def health():
    return {"status": "ok"}










