def sanitizar_entrada(entrada):
    """
    Función para sanitizar datos de entrada.
    
    Parámetros:
    - entrada (str): Cadena de texto proporcionada por el usuario.
    
    Retorna:
    - (str): Cadena de texto sanitizada.
    
    Explicación del proceso:
    1. Eliminamos espacios al inicio y al final con .strip().
    2. Permitimos solo caracteres válidos (alfanuméricos, espacios, guiones bajos y puntos) verificando uno por uno.
    3. Reemplazamos múltiples espacios consecutivos por un solo espacio.
    """
    # 1. Eliminamos espacios al inicio y al final
    entrada = entrada.strip()
    
    # 2. Definimos caracteres permitidos
    caracteres_permitidos = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._ "
    
    # 3. Construimos una nueva cadena con caracteres válidos
    entrada_sanitizada = ""
    for caracter in entrada:
        if caracter in caracteres_permitidos:
            entrada_sanitizada += caracter
    
    # 4. Reemplazamos múltiples espacios consecutivos por un solo espacio
    entrada_sanitizada = " ".join(entrada_sanitizada.split())
    
    return entrada_sanitizada

# ----------------------------------------------------------------------------------------
# -------------------------- EJEMPLO DE USO ----------------------------------------------
# ----------------------------------------------------------------------------------------

print("=== Sanitización de entrada ===")

# Entrada del usuario
entrada_usuario = input("Ingresa un texto: ")

# Aplicamos la sanitización
entrada_sanitizada = sanitizar_entrada(entrada_usuario)

print("\n=== Resultado ===")
print(f"Entrada original: {entrada_usuario}")
print(f"Entrada sanitizada: {entrada_sanitizada}")
