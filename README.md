# Gym API

🚧 Em desenvolvimento

Evolução do projeto [Gym Register](https://github.com/Renanmrqs/Gym-Register) com SQLite e FastAPI.

Estudando CS50 SQL e aplicando na prática.

---

## O que foi feito até agora

- Schema relacional com 5 tabelas (users, exercises, workouts, workouts_exercises, sets)
- Banco criado e populado com dados de exemplo
- **Segurança de ponta:** Hashing de senhas com Argon2 (padrão OWASP) e Autenticação via token JWT
- **Arquitetura modular:** Separação clara de responsabilidades (main, auth, crud, models)
- 8 queries de análise (queries.py)
- database.py — conexão segura com SQLite
- models.py — schemas Pydantic
- crud.py — funções de leitura e inserção no banco
- Rotas FastAPI (autenticação, exercises, workouts, sets)
- Deploy automatizado no Railway (utilizando variáveis de ambiente)
- Testes com pytest

## Próximos passos

- Proteger as rotas de exercícios/treinos (exigindo o token Bearer no cabeçalho)
- App Front-end no Streamlit (em desenvolvimento separado)

## Diagrama do banco de dados

![Diagrama](img/diagrama_erd.png)

## Rotas disponíveis

**Autenticação:**
- POST /register
- POST /login

**Consultas e Operações:**
- GET  /health
- GET  /exercises
- GET  /exercises/{id}
- GET  /workout_detail_w_workout/{id_workout}
- GET  /workout_detail_w_user/{id_user}
- GET  /history/{name_user}

- POST /exercises
- POST /workout
- POST /workout_exercise
- POST /sets

## API online

## API online
🔗 https://web-production-7fb8d2.up.railway.app/docs