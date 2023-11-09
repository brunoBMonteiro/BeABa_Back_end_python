def upload_to_storage(file):
    # Implemente a lógica de upload aqui
    # Por exemplo, usando a AWS S3:
    try:
        # s3_client.upload_file(...)
        return True, "Upload realizado com sucesso."
    except Exception as e:
        return False, str(e)