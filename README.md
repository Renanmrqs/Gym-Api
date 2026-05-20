# Gym API

API REST para registro e acompanhamento de treinos — evolução do [Gym Register](https://github.com/Renanmrqs/Gym-Register), que saiu de um CLI simples pra uma API com autenticação, banco relacional na nuvem, arquitetura modular e notificações em tempo real via WebSocket.

🔗 [Documentação interativa (Swagger)](https://gym-api-08pc.onrender.com/docs#/)

---

## Stack

- **FastAPI** — framework principal
- **SQLAlchemy ORM** — mapeamento objeto-relacional
- **PostgreSQL** hospedado no **Neon** — banco na nuvem
- **JWT + Argon2** — autenticação e hashing de senhas (padrão OWASP)
- **WebSocket** — notificações em tempo real (detecção de PR)
- **Deploy** no Render com variáveis de ambiente

---

## Arquitetura

```
app/
├── crud/            # operações no banco separadas por recurso
│   ├── auth.py
│   ├── exercises.py
│   └── workouts.py
├── routers/         # rotas separadas por recurso
│   ├── auth.py
│   ├── exercises.py
│   └── workouts.py
├── ws/
│   ├── manager.py   # gerenciamento de conexões WebSocket
│   └── websocket.py # rota WebSocket
├── auth.py          # lógica de autenticação JWT
├── database.py      # conexão e sessão SQLAlchemy
├── models.py        # modelos ORM (tabelas)
└── schemas.py       # schemas Pydantic (validação)
alembic/             # versionamento de migrations
```

---

## Rotas

**Autenticação:**
- `POST /register`
- `POST /login`
- `POST /logout` 🔒
- `GET /users` 🔒

**Exercises:**
- `GET /exercises`
- `GET /exercises/{id}`
- `POST /exercises` 🔒

**Workouts:**
- `GET /workout_detail_w_workout/{id_workout}` 🔒
- `GET /workout_detail_w_user/{id_user}` 🔒
- `GET /history/{name_user}` 🔒
- `POST /workout` 🔒
- `POST /workout_exercise` 🔒
- `POST /sets` 🔒 — detecta PR automaticamente e notifica via WebSocket

**WebSocket:**
- `WS /ws/{username}` — conexão persistente por usuário

🔒 requer token Bearer

---

## Notificações em Tempo Real

Quando o usuário registra uma série com peso maior que seu recorde histórico, a API detecta o PR automaticamente e envia uma notificação instantânea via WebSocket para o cliente conectado — sem necessidade de polling.

```
POST /sets  →  detecta PR  →  WebSocket envia "Parabéns! Você bateu seu PR!"
```

Cada usuário mantém sua própria conexão identificada pelo username, gerenciada pelo `ConnectionManager`.

---

## Banco de dados

Schema relacional com 5 tabelas — `users`, `exercises`, `workouts`, `workouts_exercises`, `sets`.

![Diagrama](img/diagrama_erd.png)

---

## Próximos passos

- [✅] Alembic para versionamento de migrations
- [✅] Sistema de logout completo
- [✅] Testes automatizados com pytest
- [✅] Containerização com Docker
- [✅] Notificações em tempo real com WebSocket
- [ ] Melhorar integração com o [Gym App](https://github.com/Renanmrqs/Gym-App)
