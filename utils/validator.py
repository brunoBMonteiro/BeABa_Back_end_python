import pandas as pd

def validate_file_structure(original, filled):
    original_df = pd.read_csv(original) if original.filename.endswith('.csv') else pd.read_excel(original)
    filled_df = pd.read_csv(filled) if filled.filename.endswith('.csv') else pd.read_excel(filled)

    if original_df.shape[1] != filled_df.shape[1]:
        return False, f"Número de colunas diferente. Original: {original_df.shape[1]}, Preenchido: {filled_df.shape[1]}"

    if not all(original_df.columns.str.strip().str.lower() == filled_df.columns.str.strip().str.lower()):
        return False, "Nomes das colunas não correspondem após normalização."

    for column in original_df.columns:
        # Normaliza o tipo de dados para a comparação
        original_dtype = str(original_df[column].dtype)
        filled_dtype = str(filled_df[column].dtype)
        
        # Converte tipos de dados específicos para um tipo genérico para comparação (ex: int64 e float64 para float)
        if pd.api.types.is_integer_dtype(original_dtype) and pd.api.types.is_float_dtype(filled_dtype):
            filled_dtype = 'int64'
        if pd.api.types.is_integer_dtype(filled_dtype) and pd.api.types.is_float_dtype(original_dtype):
            original_dtype = 'int64'

        if original_dtype != filled_dtype:
            return False, f"Tipo de dado incorreto na coluna '{column}'. Original: {original_dtype}, Preenchido: {filled_dtype}"

    return True, "A estrutura do arquivo é válida."