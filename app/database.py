import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()
    





# import os
# import psycopg2
# from psycopg2.extras import RealDictCursor
# from dotenv import load_dotenv

# # Carrega a URL do banco do arquivo .env
# load_dotenv()
# DATABASE_URL = os.getenv("DATABASE_URL")

# def get_connection():
#     # Conecta no Postgres da nuvem (Neon)
#     conn = psycopg2.connect(DATABASE_URL)
    
#     # Isso aqui faz o Postgres devolver as linhas como dicionários, 
#     # exatamente igual o 'conn.row_factory = sqlite3.Row' fazia!
#     return conn