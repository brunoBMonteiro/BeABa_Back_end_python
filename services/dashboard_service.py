# services/dashboard_service.py
import psycopg2
from psycopg2.extras import RealDictCursor

# Função para criar uma conexão com o banco de dados
def create_db_connection():
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )

# Função para obter a contagem de templates
def get_count_templates():
    with create_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM beaba.templates;")
            count_templates = cursor.fetchone()[0]
    return count_templates

# Função para obter a contagem de usuários
def get_count_users():
    with create_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM beaba.usuarios;")
            count_users = cursor.fetchone()[0]
    return count_users

def get_count_active_templates():
    with create_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM beaba.templates WHERE status = TRUE;")
            count_active_templates = cursor.fetchone()[0]
    return count_active_templates

def get_count_inactive_templates():
    with create_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM beaba.templates WHERE status = FALSE;")
            count_inactive_templates = cursor.fetchone()[0]
    return count_inactive_templates