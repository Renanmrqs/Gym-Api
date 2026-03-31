CREATE TABLE "users" (
    "id" INTEGER,
    "name" TEXT,
    PRIMARY KEY("id")
);

CREATE TABLE "exercises" (
    "id" INTEGER,
    "name" TEXT UNIQUE,
    PRIMARY KEY("id")
);


CREATE TABLE "workouts" (
    "id" INTEGER,
    "id_user" INTEGER,
    "datetime" NUMERIC DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY ("id"),
    FOREIGN KEY("id_user") REFERENCES "users"("id")
);

CREATE TABLE "workouts_exercises" (
    "id" INTEGER,
    "id_workout" INTEGER,
    "id_exercise" INTEGER,
    PRIMARY KEY ("id"),
    FOREIGN KEY("id_workout") REFERENCES "workouts"("id"),
    FOREIGN KEY("id_exercise") REFERENCES "exercises"("id")
);


CREATE TABLE "sets" (
"id" INTEGER,
"id_workout_exercise" INTEGER,
"weight" NUMERIC NOT NULL CHECK("weight" != 0),
"reps" NUMERIC NOT NULL CHECK("reps" != 0),
PRIMARY KEY ("id"),
FOREIGN KEY("id_workout_exercise") REFERENCES "workouts_exercises"("id")
);
