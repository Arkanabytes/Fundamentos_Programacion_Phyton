import hashlib

def anonimizar_datos(datos):
    """
    Anonimiza una lista de datos reemplazándolos por un valor genérico.
    Parámetros:
    - datos (list): Lista de cadenas (por ejemplo, nombres).

    Retorna:
    - list: Lista de valores anonimizados.
    """
    return ["Usuario Anónimo" for _ in datos]

def seudonimizar_datos(datos, clave_secreta="mi_clave_segura"):
    """
    Seudonimiza una lista de datos utilizando un hash seguro. 
    Parámetros:
    - datos (list): Lista de cadenas (por ejemplo, nombres).
    - clave_secreta (str): Clave usada para generar los hashes (evita colisiones entre sistemas).
    
    Retorna:
    - list: Lista de valores seudonimizados.
    """
    seudonimos = []
    for dato in datos:
        # Concatenamos el dato con la clave secreta
        combinado = dato + clave_secreta
        # Creamos un hash único usando SHA-256
        hash_dato = hashlib.sha256(combinado.encode()).hexdigest()
        # Usamos una parte del hash como seudónimo
        seudonimos.append(hash_dato[:10])  # Usamos los primeros 10 caracteres del hash
    return seudonimos

# ----------------------------------------------------------------------------------------
# -------------------------- EJEMPLO DE USO ----------------------------------------------
# ----------------------------------------------------------------------------------------

# Lista de nombres originales
nombres = ["Alex", "Ester", "Armando", "Javiera"]

print("=== Original ===")
print(nombres)

# Anonimización
nombres_anonimizados = anonimizar_datos(nombres)
print("\n=== Anonimización ===")
print(nombres_anonimizados)

# Seudonimización
nombres_seudonimizados = seudonimizar_datos(nombres)
print("\n=== Seudonimización ===")
print(nombres_seudonimizados)
