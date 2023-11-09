from utils.validator import validate_file_structure

def validate_and_save_template(original, filled):
    # A função validate_file_structure é chamada com ambos os arquivos como argumentos
    is_valid, message = validate_file_structure(original, filled)
    
    if is_valid:
        # Aqui você pode implementar a lógica de salvar o arquivo em um armazenamento
        return True, 'Arquivos validados com sucesso.'
    else:
        return False, message
