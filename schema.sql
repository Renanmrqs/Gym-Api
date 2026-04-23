DROP TABLE IF EXISTS "users" CASCADE;
DROP TABLE IF EXISTS "exercises" CASCADE;
DROP TABLE IF EXISTS "sets" CASCADE;
DROP TABLE IF EXISTS "workouts_exercises" CASCADE;
DROP TABLE IF EXISTS "workouts" CASCADE;
DROP VIEW IF EXISTS "workout_summary" CASCADE;

CREATE TABLE "users" (
    "id" bigint GENERATED ALWAYS AS IDENTITY,
    "name" TEXT UNIQUE NOT NULL,
    "password" TEXT NOT NULL,
    PRIMARY KEY("id")
);

CREATE TABLE "exercises" (
    "id" bigint GENERATED ALWAYS AS IDENTITY,
    "name" TEXT UNIQUE,
    PRIMARY KEY("id")
);


CREATE TABLE "workouts" (
    "id" bigint GENERATED ALWAYS AS IDENTITY,
    "id_user" INTEGER,
    "datetime" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY ("id"),
    FOREIGN KEY("id_user") REFERENCES "users"("id")
);

CREATE TABLE "workouts_exercises" (
    "id" bigint GENERATED ALWAYS AS IDENTITY,
    "id_workout" INTEGER,
    "id_exercise" INTEGER,
    PRIMARY KEY ("id"),
    FOREIGN KEY("id_workout") REFERENCES "workouts"("id"),
    FOREIGN KEY("id_exercise") REFERENCES "exercises"("id")
);


CREATE TABLE "sets" (
"id" bigint GENERATED ALWAYS AS IDENTITY,
"id_workout_exercise" INTEGER,
"weight" NUMERIC NOT NULL CHECK("weight" != 0),
"reps" NUMERIC NOT NULL CHECK("reps" != 0),
PRIMARY KEY ("id"),
FOREIGN KEY("id_workout_exercise") REFERENCES "workouts_exercises"("id")
);

CREATE VIEW workout_summary AS 
SELECT
    users.name as user,
    exercises.name as exercise,
    workouts.datetime,
    sets.weight,
    sets.reps
FROM sets
JOIN workouts_exercises ON workouts_exercises.id = sets.id_workout_exercise
JOIN exercises ON exercises.id = workouts_exercises.id_exercise
JOIN workouts on workouts.id = workouts_exercises.id_workout
JOIN users on users.id = workouts.id_user;