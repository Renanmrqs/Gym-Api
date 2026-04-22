from psycopg2.extras import RealDictCursor
from app.auth import pwd_context
from app.database import get_connection

connect = get_connection()


# connect = get_connection()

# # 2. Abre o cursor (obrigatório no Postgres)
# cursor = connect.cursor()

# # 3. Lê o arquivo
# with open("schema.sql", 'r') as f:
#     schema = f.read() 

# # 4. Executa o SQL
# cursor.execute(schema)

# # 5. Salva de verdade (Isso é obrigatório no Postgres!)
# connect.commit()

# # 6. Fecha as portas
# cursor.close()
# connect.close()

print('Tabelas criadas com sucesso no Postgres!')


with open("seed.sql", 'r') as f:
    seed = f.read() 

cursor = connect.cursor()
cursor.execute(seed)
connect.commit()


### migrando login dos users
def migrate_users():
    conn = get_connection()
    # 1. Abre o cursor pedindo para devolver como dicionário
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    # 2. Roda a query (não precisa de 'users = ' antes)
    cur.execute('SELECT * FROM "users";')
    
    # 3. Pega os resultados (já vai vir como uma lista de dicionários!)
    users = cur.fetchall()
    print(users)
    
    for user in users:
        senha_atual = pwd_context.hash(user["password"])
        cur.execute("""
        UPDATE "users" SET password = %s 
        WHERE id = %s;            
        """, (senha_atual, user["id"]))

migrate_users()
cursor.close()
connect.close()

print('adicioned')