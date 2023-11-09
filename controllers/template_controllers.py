from flask import Blueprint, request, jsonify
from services.template_service import validate_and_save_template

template_blueprint = Blueprint('template_blueprint', __name__)

@template_blueprint.route('/validate-template', methods=['POST'])
def validate_template():
    original_file = request.files['originalTemplate']
    filled_file = request.files['filledTemplate']
    is_valid, message = validate_and_save_template(original_file, filled_file)

    if is_valid:
        return jsonify({'status': 'approved', 'message': 'Template aprovado!'}), 200
    else:
        return jsonify({'status': 'error', 'message': message}), 400
