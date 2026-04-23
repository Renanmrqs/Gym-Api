from app.database import get_connection
from psycopg2.extras import RealDictCursor
# READS:

# busca todos usuarios e id cadastrado

def get_users():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    cur.execute('SELECT * FROM "users"') 
    rows = cur.fetchall()
    return rows

# busca usuario especifico atraves do nome
def get_users_by_name(name):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(""" 
    SELECT * FROM "users"
    WHERE name = %s  
    """, (name,)) 
    row = cur.fetchone()
    return row


# buscar o historico pelo nome do usuario
def get_historic(name_user):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(""" 
    SELECT * FROM "workout_summary"
    WHERE user = %s
    """, (name_user,))
    rows = cur.fetchall()
    return rows


# busca todos os exercicios
def get_exercises():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("""
    SELECT * FROM "exercises" 
    """)
    rows = cur.fetchall()
    return rows

# busca exercicio filtrando por id

def get_exercises_id(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("""
    SELECT "name" FROM "exercises" 
    WHERE id = %s
    """, (id,))
    rows = cur.fetchall()
    return rows

# treinos de um ususario com data

def get_exercicios_users(name):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("""
    SELECT "users"."name", "exercises"."name", "workouts"."datetime" 
    FROM workouts_exercises
    JOIN "users" ON "users"."id" = "workouts"."id_user"
    JOIN 'workouts' ON "workouts"."id" = "workouts_exercises"."id_workout"
    JOIN "exercises" ON "exercises"."id" = "workouts_exercises"."id_exercise"
    WHERE "users"."name" = %s
    """, (name,))
    rows = cur.fetchall()
    return rows


# busca treinos filtrando por usuario
def get_workouts_by_user(user_id): 
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("""
    SELECT datetime FROM "workouts"
    WHERE "id_user" = %s
    """, (user_id,))
    rows = cur.fetchall()
    return rows

# busca exercicio filtrando por id de treino
def get_workout_detail(workout_id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("""
    SELECT "workouts_exercises"."id", "workouts_exercises"."id_workout", "exercises"."name" 
    FROM "workouts_exercises"
    JOIN "exercises" ON "exercises"."id" = "workouts_exercises"."id_exercise"
    WHERE "id_workout" = %s
    """, (workout_id,))
    rows = cur.fetchall()
    return rows

#CREATES:

# adiciona na tabela exercicios
def create_exercise(name):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("""
        INSERT INTO "exercises" ("name")
        VALUES
        (%s);
        """, (name,))
        conn.commit()
    finally:
        conn.close()


# cria um dia de treino
def create_workout(user_id):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("""
        INSERT INTO "workouts" ("id_user")
        VALUES
        (%s);
        """, (user_id,))
        conn.commit()
        workout_id = cur.lastrowid
    finally:
        conn.close()
    return workout_id

# adiciona um exercicio em um dia de treino
def create_workout_exercise(workout_id, exercise_id):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("""
        INSERT INTO "workouts_exercises" ("id_workout", "id_exercise")
        VALUES
        (%s, %s);
        """, (workout_id, exercise_id))
        conn.commit()
        workout_exercise_id = cur.lastrowid
    finally:
        conn.close()
    return workout_exercise_id

# adiciona na tabela sets 
def create_set(workout_exercise_id, weight, reps):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("""
        INSERT INTO "sets" ("id_workout_exercise", "weight", "reps")
        VALUES
        (%s, %s, %s);
        """, (workout_exercise_id, weight, reps))
        conn.commit()
    finally:
        conn.close()
    
# adiciona um user na tabela user
def create_register(name, password):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("""
        INSERT INTO "users" ("name", "password")
        VALUES
        (%s, %s);
        """, (name, password))
        conn.commit()
    finally:
        conn.close()
    

