import sqlite3

conn = sqlite3.connect('gym.db')
cur = conn.cursor()


cur.execute("""
    SELECT 
    users.name, 
    exercises.name, 
    workouts.datetime 
    FROM workouts_exercises 
    JOIN 'exercises' ON 'exercises'.'id' = 'workouts_exercises'.'id_exercise' JOIN 'workouts' ON 'workouts'.'id' = 'workouts_exercises'.'id_workout' JOIN 'users' ON 'users'.'id' = 'workouts'.'id_user' 
    """)
cur.execute("SELECT FROM users")

# cur.execute("""
#     SELECT 
#         weight * reps FROM sets
#     JOIN 'exercises' ON 'exercises'.'id' = 'workouts_exercises'.'id_exercise' JOIN 'workouts' ON 'workouts'.'id' = 'workouts_exercises'.'id_workout'
#     GROUP BY (name, exercise) 
#             """)

print(cur.fetchall())
conn.close()
"""
Todos os treinos de um usuário com data.
Todos os exercícios de um treino específico.
Volume total por exercício (weight * reps somado) em um treino.
Evolução do peso máximo num exercício ao longo do tempo.
Frequência de cada exercício (quantas vezes aparece nos treinos).
"""