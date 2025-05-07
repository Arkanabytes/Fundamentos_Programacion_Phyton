def valida_nombre(texto)->str:
    """Esta función verifica si un nombre de archivo es seguro.

    Parámetros:
        texto (str): Texto que corresponde al nombre de archivo ingresado por el usuario

    Retorno:
        str: Cadena de texto que corresponde al mensaje de respuesta al usuario
    """
    # Caracteres no permitidos
    caracteres_no_permitidos = ["../", "..\\", ":", "*", "?", "<", ">", "|"]
    # Verificamos si contiene caracteres no permitidos
    if any(caracter in texto for caracter in caracteres_no_permitidos):
        return "El nombre de archivo contiene caracteres no permitidos. ¡Revisa tu entrada!"
    else:
        return "El nombre de archivo es seguro."

# Solicitamos al usuario un nombre de archivo
nombre_archivo = input("Ingresa un nombre de archivo: ")
print(valida_nombre(nombre_archivo))


