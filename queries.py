import sqlite3

conn = sqlite3.connect('gym.db')
cur = conn.cursor()

print('frequencia de cada exercicio: ')
cur.execute("""
    SELECT "exercises"."name", COUNT("exercises"."name")
    FROM "sets" 
    JOIN "workouts_exercises" ON  "workouts_exercises"."id_exercise" = "sets"."id_workout_exercise" 
    JOIN "exercises" ON "exercises"."id" = "workouts_exercises"."id_exercise" 
    GROUP BY "exercises"."name"

    """)
print(cur.fetchall())
print()

print('Evolução de pesos num exercício')
cur.execute("""
    SELECT "exercises"."name", weight
    FROM "sets" 
    JOIN "workouts_exercises" ON  "workouts_exercises"."id_exercise" = "sets"."id_workout_exercise" 
    JOIN "exercises" ON "exercises"."id" = "workouts_exercises"."id_exercise" 
    JOIN  "workouts" ON  "workouts"."id" = "workouts_exercises"."id_workout" 

    """)
print(cur.fetchall())
print()

print('Volume total por exercício em um treino: ')
cur.execute("""
    SELECT "exercises"."name", SUM("weight" * "reps")
    FROM "sets" 
    JOIN "workouts_exercises" ON  "workouts_exercises"."id_exercise" = "sets"."id_workout_exercise" 
    JOIN "exercises" ON "exercises"."id" = "workouts_exercises"."id_exercise" 
    GROUP BY "exercises"."name"

    """)
print(cur.fetchall())
print()

print('Todos os exercícios de um treino específico: ')
cur.execute("""
    SELECT "exercises"."name", "workouts"."id" 
    FROM "workouts_exercises" 
    JOIN "exercises" ON "exercises"."id" = "workouts_exercises"."id_exercise" 
    JOIN  "workouts" ON  "workouts"."id" = "workouts_exercises"."id_workout"
    WHERE "workouts"."id" = 1
    """)
print(cur.fetchall())
print()

print('Todos os treinos de um usuário com data:')
cur.execute("""
    SELECT "users"."name", "exercises"."name", "workouts"."datetime" 
    FROM workouts_exercises
    JOIN "users" ON "users"."id" = "workouts"."id_user"
    JOIN 'workouts' ON "workouts"."id" = "workouts_exercises"."id_workout"
    JOIN "exercises" ON "exercises"."id" = "workouts_exercises"."id_exercise"
    WHERE "users"."name" = "Renan"
            """)
print(cur.fetchall())
print()

print('Total de séries por treino')
cur.execute("""
    SELECT COUNT(sets.id) as "TOTAL DE SÉRIES POR TREINO", 
    "workouts"."id"
    FROM sets
    JOIN "workouts" ON "workouts"."id" = "workouts_exercises"."id_workout"
    JOIN "workouts_exercises" ON "workouts_exercises"."id" = "sets"."id_workout_exercise"
    GROUP BY "workouts"."id" 
    
            """)
print(cur.fetchall())
print()

print('top set de cada exercicio')
cur.execute("""
    SELECT "exercises"."name", MAX(weight) as total
    FROM sets
    JOIN "exercises" ON "exercises"."id" = "workouts_exercises"."id_exercise"
    JOIN "workouts" ON "workouts"."id" = "workouts_exercises"."id_workout"
    JOIN "workouts_exercises" ON "workouts_exercises"."id" = "sets"."id_workout_exercise"
    GROUP BY "exercises"."name"
    ORDER BY total DESC
            """)
print(cur.fetchall())
print()

print('media de reps por treino')
cur.execute("""
    SELECT ROUND(AVG("sets"."reps"), 2)
    FROM sets
    JOIN "exercises" ON "exercises"."id" = "workouts_exercises"."id_exercise"
    JOIN "workouts" ON "workouts"."id" = "workouts_exercises"."id_workout"
    JOIN "workouts_exercises" ON "workouts_exercises"."id" = "sets"."id_workout_exercise"
    
            """)
print(cur.fetchall())
print()

conn.close()
"""
Todos os treinos de um usuário com data.
Todos os exercícios de um treino específico.
Volume total por exercício (weight * reps somado) em um treino.
Evolução do peso máximo num exercício ao longo do tempo.
Frequência de cada exercício (quantas vezes aparece nos treinos).
"""