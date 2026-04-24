from fastapi import FastAPI
# , exceptions, HTTPException, security, Depends
from app.routers import exercises
# from app.auth import pwd_context, generate_token, verify_token


app = FastAPI()
app.include_router(exercises.router)

# security_rote = security.OAuth2PasswordBearer(tokenUrl="login")
# def get_current_user(token: str = Depends(security_rote)):
#     user  = verify_token(token)
#     return user

# # READS
# # cria a rota padrao
# @app.get("/health")
# def health():
#     return {"status": "ok"}

#cria a rota de puxar o exercicio


# @app.get("/exercises")
# def read_exercises():
#     return get_exercises()

# # cria a rota de puxar exercicio por id
# @app.get("/exercises/{id}")
# def read_exercises_detail(id: int):
#     return get_exercises_id(id)


# # cria a rota de puxa o treino de acordo com o id de treino 
# @app.get("/workout_detail_w_workout/{id_workout}")
# def read_workout_detail_workout(id_workout: int):
#     return get_workout_detail(id_workout)

# # cria a rota de puxa o treino de acordo com o id do user
# @app.get("/workout_detail_w_user/{id_user}")
# def read_workout_detail_user(id_user: int):
#     return get_workouts_by_user(id_user)


# # faz a rota de puxar o historico de sets completo com o nome
# @app.get("/history/{name_user}")
# def read_history_sets_by_user(name_user: str):
#     result = get_historic(name_user)
#     if not result:
#         raise exceptions.HTTPException(status_code=400, detail=f'{name_user} not in table')
#     return result

# # faz a rota de puxar tudo da tabela usuarios 
# @app.get("/users")
# def read_users():
#     return get_users()

# # CREATES
# # faz a rota de adicionar exercicio na tabela exercicios
# @app.post("/exercises")
# def post_exercise(exercise: ExerciseCreate, user: str = Depends(get_current_user)):
#     try:
#         create_exercise(exercise.name)
#         return {"message": f"exercise {exercise.name} Created by {user}"}
#     except sqlite3.IntegrityError:
#         raise HTTPException(status_code=400, detail=f"{exercise.name} already in the table")

# # faz a rota de criar treino 
# @app.post("/workout")
# def post_workout(workout: WorkoutCreate, user: str = Depends(get_current_user)):
#     try:
#         workout_id = create_workout(workout.id_user)
#         return {"message": "Workout Created", "id": workout_id}
#     except sqlite3.IntegrityError:
#         raise HTTPException(status_code=400, detail=f'{workout.id_user} not in the table')

# # faz a rota de adicionar exercicio no treino
# @app.post("/workout_exercise")
# def post_add_exercise_in_workout(workout_exercise: WorkoutsExercisesCreate, user: str = Depends(get_current_user)):
#     try:
#         workout_exercise_id = create_workout_exercise(workout_exercise.id_workout, workout_exercise.id_exercise)
#         return {"message": "Exercise added in workout", "id": workout_exercise_id}
#     except sqlite3.IntegrityError:
#         raise HTTPException(status_code=400, detail="Workout or Exercise ID not found, or already added.")

# # faz a rota de registrar a série
# @app.post("/sets")
# def post_sets(sets: SetsCreate, user: str = Depends(get_current_user)):
#     try:
#         create_set(sets.id_workout_exercise, sets.weight, sets.reps)
#         return {"message": f"Exercise add weight: {sets.weight} | reps: {sets.reps}"}
#     except sqlite3.IntegrityError:
#         raise HTTPException(status_code=400, detail=f'{sets.id_workout_exercise} not in the table')


# #####registro de usuario
# ##faz a rota de criar o registro    
# @app.post("/register")
# def post_register(register: LoginRequest):
#     try:
#         password_criptografed = pwd_context.hash(register.password)

#         create_register(register.name, password_criptografed)
        
#         return {"message": f"user {register.name} registred"}
#     except sqlite3.IntegrityError:
#         raise HTTPException(status_code=400, detail=f'{register.name} already in table')

# # faz rota do usuario logar na aplicacao
# @app.post("/login")
# def post_login(form_data: security.OAuth2PasswordRequestForm = Depends()):
#     login_return = get_users_by_name(form_data.username)
#     if not login_return:
#         raise exceptions.HTTPException(status_code=400, detail=f'{form_data.username} is not registred')
    
#     password_corrrect = pwd_context.verify(form_data.password, login_return["password"])
#     if password_corrrect == False:
#         raise exceptions.HTTPException(status_code=400, detail=f'incorrect password, try again.')
    
#     token = generate_token(form_data.username)
    
#     return {"access_token": token, "token_type": "bearer", "user_id": login_return['id']}

