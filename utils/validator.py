import pandas as pd

def validate_file_structure(original, filled):
    # Acesse o nome do arquivo para verificar a extensão
    original_filename = original.filename
    filled_filename = filled.filename

    # Verifica se os nomes dos arquivos são iguais
    if original_filename != filled_filename:
        return False, "Os nomes dos arquivos são diferentes."

    # Use a extensão do arquivo para determinar como ler
    if original_filename.endswith('.csv'):
        original_df = pd.read_csv(original)
        filled_df = pd.read_csv(filled)
    elif original_filename.endswith('.xls') or original_filename.endswith('.xlsx'):
        original_df = pd.read_excel(original)
        filled_df = pd.read_excel(filled)
    else:
        return False, "Formato de arquivo não suportado."

    # Imprime os nomes das colunas para depuração
    print("Colunas originais:", original_df.columns.tolist())
    print("Colunas preenchidas:", filled_df.columns.tolist())

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

    return True, "A estrutura do arquivo é válida."