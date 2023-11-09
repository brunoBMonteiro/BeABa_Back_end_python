from utils.validator import validate_file_details

def validate_and_save_template(original, filled):
    if not validate_file_details(original) or not validate_file_details(filled):
        return False, 'Detalhes do arquivo inválidos.'

    # Aqui você pode implementar a lógica de salvar o arquivo em um armazenamento

    return True, 'Arquivos validados com sucesso.'
