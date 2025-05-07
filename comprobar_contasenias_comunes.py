from getpass import getpass

def comprobar_contrasenia(texto)->str:
    """Esta funcion verifica si una contraseña ingresada pertenece a una lista de contraseñas comunes

    Parámetros:
        texto (str): Texto que corresponde a la contraseña ingresada por el usuario

    Retorno:
        str: Cadena de texto que corresponde al mensaje de respuesta al usuario 
    """
    # Lista de contraseñas comunes
    contrasenias_comunes = ["123456", "password", "12345678", "qwerty", "Ventana#123"]
    # Verificar si está en la lista de contraseñas comunes
    if texto in contrasenias_comunes:
        return f"La contraseña {texto} es muy común. ¡No es segura!"
    else:
        return f"La contraseña {texto} no está en la lista de las comunes. Es mejor."

# Solicitar al usuario una contraseña
contrasenia = getpass("Ingresa una contraseña para verificar: ")
print(comprobar_contrasenia(contrasenia))
