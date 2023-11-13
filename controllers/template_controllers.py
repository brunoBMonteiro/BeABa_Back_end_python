from flask import Blueprint, request, jsonify, abort
from flask_cors import CORS
from services.template_service import validate_and_save_template

template_blueprint = Blueprint('template_blueprint', __name__)
CORS(template_blueprint)

@template_blueprint.route('/validate-template', methods=['POST'])
def validate_template():
    try:
        # Tenta pegar os arquivos enviados
        original_file = request.files.get('originalTemplate')
        filled_file = request.files.get('filledTemplate')

        # Se algum dos arquivos não for fornecido, retorna um erro 400
        if not original_file or not filled_file:
            abort(400, description="Arquivos para validação não foram fornecidos.")

        # Se os arquivos forem fornecidos, tenta validar
        is_valid, message = validate_and_save_template(original_file, filled_file)
        
        # Se for válido, retorna status 200
        if is_valid:
            return jsonify({'status': 'approved', 'message': 'Template aprovado!'}), 200
        else:
            # Se a validação falhar, retorna status 400 com a mensagem de erro
            abort(400, description=message)
            
    except Exception as e:
        # Se ocorrer uma exceção não capturada nos blocos anteriores, retorna status 500
        abort(500, description=str(e))