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

def get_dashboard_data():
    with create_db_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("""
                SELECT 
                    t.id_template,
                    t.nome_template,
                    t.extensao_template,
                    t.data_cadastrado,
                    t.status,
                    t.quantidade_linhas,
                    t.campos_template,
                    u.id_usuario as "id_usuario_cadastrado",
                    u.matricula,
                    u.email,
                    u.nome_usuario
                FROM 
                    beaba.templates t
                JOIN 
                    beaba.usuarios u ON t.id_usuario_cadastrado = u.id_usuario;
            """)
            dashboard_data = cursor.fetchall()
    return dashboard_data