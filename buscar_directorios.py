import os

def verifica_directorios(texto)->str:
    """Esta función comprueba si un archivo o carpeta existe en un sistema local.

    Parámetros:
        texto (str): Texto que corresponde a la ruta ingresada por el usuario

    Retorno:
        str: Cadena de texto que corresponde al mensaje de respuesta al usuario
    """
    # Verificar si existe
    if os.path.exists(texto):
        return f"La ruta '{texto}' existe en el sistema."
    else:
        return f"La ruta '{texto}' no existe."

# Solicitar al usuario un nombre de archivo o carpeta
ruta = input("Ingresa la ruta de un archivo o carpeta: ")
print(verifica_directorios(ruta))