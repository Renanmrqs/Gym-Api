INSERT INTO "users" ("name")
VALUES 
('Renan'),
('Joaquim');

INSERT INTO "exercises" ("name")
VALUES 
('Agachamento Livre'),
('Levantamento Terra'),
('Leg Press'),
('Mesa Flexora'),
('Panturrilha Escada'),
('Abdominal Infra');

INSERT INTO "workouts" ("id_user", "datetime")
VALUES 
('1', '2026-03-10 10:00:00');

INSERT INTO "workouts_exercises" ("id_workout", "id_exercise")
VALUES
('1', '1'),
('1', '2');

INSERT INTO "sets" ("id_workout_exercise", "weight", "reps")
VALUES
('1', '30', '10'),
('1', '50', '8'),
('1', '60', '6'),
('2', '60', '6'),
('2', '80', '4');