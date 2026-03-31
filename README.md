# Gym API

🚧 Em desenvolvimento

Evolução do projeto [Gym Register](https://github.com/Renanmrqs/Gym-Register) com SQLite e FastAPI.

Estudando CS50 SQL e aplicando na prática.

---

## O que foi feito até agora

- Schema relacional com 5 tabelas (users, exercises, workouts, workouts_exercises, sets)
- Banco criado e populado com dados de exemplo
- 8 queries de análise (queries.py)
- database.py — conexão com SQLite
- models.py — schemas Pydantic
- crud.py — funções de leitura e inserção no banco
- Rotas FastAPI (exercises, workouts, sets) 
- Deploy no Railway

## Próximos passos

- criar novas rotas, com crud completo
- criação de app 100% completo consumindo a api e o banco de dados

## Diagrama do banco de dados

![ERD](file:///C:/Users/renan/Downloads/gym_api_schema.svg)

## Rotas disponíveis

GET  /health
GET  /exercises
GET  /exercises/{id}
GET  /workout_detail_w_workout/{id_workout}
GET  /workout_detail_w_user/{id_user}

POST /exercises
POST /workout
POST /workout_exercise
POST /sets

## API online
🔗 https://web-production-7fb8d2.up.railway.app/docs