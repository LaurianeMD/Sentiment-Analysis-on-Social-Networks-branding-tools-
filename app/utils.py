# from datetime import datetime

# def validate_date(date_str: str) -> datetime:
#     try:
#         # Convertir la chaîne en objet datetime en utilisant le format spécifié
#         return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
#     except ValueError:
#         # Lever une exception si le format est incorrect
#         raise ValueError("Incorrect date format, should be YYYY-MM-DDTHH:MM:SS")



from datetime import datetime

def validate_date(date_str: str) -> datetime:
    try:
        # Convertir la chaîne en objet datetime en utilisant le format spécifié
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
    except ValueError:
        # Lever une exception si le format est incorrect
        raise ValueError("Incorrect date format, should be YYYY-MM-DDTHH:MM:SS")
