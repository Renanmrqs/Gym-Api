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

## Próximos passos

- Rotas FastAPI (exercises, workouts, sets)
- Deploy no Railway

## Como rodar
```bash
python create_db.py  # cria o banco
python seed.py       # popula com dados de exemplo
```