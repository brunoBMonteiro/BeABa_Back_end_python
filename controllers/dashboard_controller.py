from flask import Blueprint, jsonify, abort
from services.dashboard_service import get_count_templates, get_count_users
import psycopg2

dashboard_blueprint = Blueprint('dashboard_blueprint', __name__)

@dashboard_blueprint.route('/count-templates', methods=['GET'])
def count_templates_endpoint():
    try:
        count = get_count_templates()
        if count or count == 0:  # Inclui o cenário onde a contagem é zero
            return jsonify({'total_templates': count}), 200
        else:
            abort(404, description="Nenhum template encontrado.")
    except psycopg2.DatabaseError as db_err:
        # Log do erro no banco de dados
        abort(500, description="Erro de banco de dados: " + str(db_err))
    except Exception as e:
        # Log de outras exceções
        abort(500, description="Erro interno do servidor: " + str(e))

@dashboard_blueprint.route('/count-users', methods=['GET'])
def count_users_endpoint():
    try:
        count = get_count_users()
        if count or count == 0:  # Inclui o cenário onde a contagem é zero
            return jsonify({'total_users': count}), 200
        else:
            abort(404, description="Nenhum usuário encontrado.")
    except psycopg2.DatabaseError as db_err:
        # Log do erro no banco de dados
        abort(500, description="Erro de banco de dados: " + str(db_err))
    except Exception as e:
        # Log de outras exceções
        abort(500, description="Erro interno do servidor: " + str(e))