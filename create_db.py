from app.database import get_connection

connect = get_connection()

# 2. Abre o cursor (obrigatório no Postgres)
cursor = connect.cursor()

# 3. Lê o arquivo
with open("schema.sql", 'r') as f:
    schema = f.read() 

# 4. Executa o SQL
cursor.execute(schema)

# 5. Salva de verdade (Isso é obrigatório no Postgres!)
connect.commit()

# 6. Fecha as portas
cursor.close()
connect.close()

print('Tabelas criadas com sucesso no Postgres!')