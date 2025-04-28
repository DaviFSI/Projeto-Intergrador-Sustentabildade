import mysql.connector
from dotenv import load_dotenv
import os

# Carrega variáveis do .env
load_dotenv()

# Agora pode acessar normalmente:
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
db_host = os.getenv('DB_HOST')


print(f"Conectando com o usuário {db_user}")

conexao = mysql.connector.connect(
    host=db_host,
    user=db_user,           # ou o usuário que você definiu
    password=db_password,
    database=db_name 
)

cursor = conexao.cursor(dictionary=True)