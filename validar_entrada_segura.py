def valida_entrada(texto)->str:
    """Esta función verifica si una entrada de texto contiene comandos sospechosos que podrían ser peligrosos.

    Parámetros:
        texto (str): Texto que corresponde a la entrada ingresada por el usuario

    Retorno:
        str: Cadena de texto que corresponde al mensaje de respuesta al usuario
    """
    # Lista de palabras sospechosas
    palabras_sospechosas = ["delete", "drop", "shutdown", ";", "--"]

    # Verificar si contiene palabras sospechosas
    if any(palabra in texto for palabra in palabras_sospechosas):
        return "La entrada contiene palabras sospechosas. Podría ser insegura."
    else:
        return "La entrada parece segura."

# Solicitamos una entrada del usuario
entrada_usuario = input("Ingresa un texto: ")
print(valida_entrada(entrada_usuario))
