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
JOIN users on users.id = workouts.id_user