from flask import Blueprint, jsonify, abort
from services.dashboard_service import (
    get_count_templates, 
    get_count_users,  
    get_count_active_templates,
    get_count_inactive_templates,
    get_dashboard_data
)
import psycopg2

dashboard_blueprint = Blueprint('dashboard_blueprint', __name__)

@dashboard_blueprint.route('/count-templates', methods=['GET'])
def count_templates_endpoint():
    try:
        count = get_count_templates()
        return jsonify({'total_templates': count}), 200
    except psycopg2.DatabaseError as db_err:
        abort(500, description="Erro de banco de dados: " + str(db_err))
    except Exception as e:
        abort(500, description="Erro interno do servidor: " + str(e))       

@dashboard_blueprint.route('/count-users', methods=['GET'])
def count_users_endpoint():
    try:
        count = get_count_users()
        return jsonify({'total_users': count}), 200
    except psycopg2.DatabaseError as db_err:
        abort(500, description="Erro de banco de dados: " + str(db_err))
    except Exception as e:
        abort(500, description="Erro interno do servidor: " + str(e)) 
        
@dashboard_blueprint.route('/count-active-templates', methods=['GET'])
def count_active_templates_endpoint():
    try:
        count = get_count_active_templates()
        return jsonify({'total_active_templates': count}), 200
    except psycopg2.DatabaseError as db_err:
        abort(500, description="Erro de banco de dados: " + str(db_err))
    except Exception as e:
        abort(500, description="Erro interno do servidor: " + str(e))

@dashboard_blueprint.route('/count-inactive-templates', methods=['GET'])
def count_inactive_templates_endpoint():
    try:
        count = get_count_inactive_templates()
        return jsonify({'total_inactive_templates': count}), 200
    except psycopg2.DatabaseError as db_err:
        abort(500, description="Erro de banco de dados: " + str(db_err))
    except Exception as e:
        abort(500, description="Erro interno do servidor: " + str(e))
        
@dashboard_blueprint.route('/dashboard-data', methods=['GET'])
def dashboard_data():
    try:
        data = get_dashboard_data()
        return jsonify(data), 200
    except psycopg2.DatabaseError as db_err:
        abort(500, description="Erro de banco de dados: " + str(db_err))
    except Exception as e:
        abort(500, description="Erro interno do servidor: " + str(e))