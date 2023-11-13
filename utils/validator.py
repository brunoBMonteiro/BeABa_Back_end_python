import pandas as pd
import os

def validate_file_structure(original, filled):
    # Extrai o nome do arquivo e a extensão para verificar
    original_filename, original_extension = os.path.splitext(original.filename)
    filled_filename, filled_extension = os.path.splitext(filled.filename)

    # Verifica se os nomes dos arquivos são iguais
    if original_filename != filled_filename:
        return False, "Os nomes dos arquivos são diferentes."

    # Verifica se as extensões dos arquivos são iguais
    if original_extension != filled_extension:
        return False, "As extensões dos arquivos são diferentes."

    try:
        # Trata arquivos CSV
        if original_extension == '.csv':
            original_df = pd.read_csv(original)
            filled_df = pd.read_csv(filled)
        # Trata arquivos XLS
        elif original_extension == '.xls':
            # Especifica o engine 'xlrd' para ler arquivos .xls
            original_df = pd.read_excel(original, engine='xlrd')
            filled_df = pd.read_excel(filled, engine='xlrd')
        # Trata arquivos XLSX
        elif original_extension == '.xlsx':
            # Especifica o engine 'openpyxl' para ler arquivos .xlsx
            original_df = pd.read_excel(original, engine='openpyxl')
            filled_df = pd.read_excel(filled, engine='openpyxl')
        else:
            return False, "Formato de arquivo não suportado."

        # Verifica se o número de colunas é igual
        if original_df.shape[1] != filled_df.shape[1]:
            return False, f"Número de colunas diferente. Original: {original_df.shape[1]}, Preenchido: {filled_df.shape[1]}"

        # Verifica se os nomes das colunas são iguais
        if not original_df.columns.equals(filled_df.columns):
            return False, f"Nomes das colunas diferentes. Original: {original_df.columns.tolist()}, Preenchido: {filled_df.columns.tolist()}"

        # Verifica os tipos de dados das colunas
        for column in original_df.columns:
            if original_df[column].dtype != filled_df[column].dtype:
                return False, f"Tipo de dado incorreto na coluna '{column}'. Original: {original_df[column].dtype}, Preenchido: {filled_df[column].dtype}"

    except Exception as e:
        # Aqui vamos capturar o erro e imprimir mais informações para ajudar no diagnóstico
        error_message = f"Erro ao processar os arquivos: {type(e).__name__}, {e}"
        print(error_message)  # ou use um logger se tiver um configurado
        return False, error_message

    # Se todas as verificações passaram, retorna True e a mensagem de sucesso
    return True, "A estrutura do arquivo é válida."