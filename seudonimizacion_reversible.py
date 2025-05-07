from cryptography.fernet import Fernet

# Generar o cargar una clave secreta única
#  en caso de contar con una clave, guárdala para usarla posteriormente
clave_secreta = Fernet.generate_key()
cifrador = Fernet(clave_secreta)

def seudonimizar_datos_reversibles(datos):
    """
    Seudonimiza datos mediante cifrado para que puedan ser revertidos.
    
    Parámetros:
    - datos (list): Lista de cadenas (por ejemplo, nombres).
    
    Retorna:
    - list: Lista de datos cifrados (seudonimizados).
    """
    seudonimos = [cifrador.encrypt(dato.encode()).decode() for dato in datos]
    return seudonimos

def revertir_seudonimos(seudonimos):
    """
    Revierte los datos seudonimizados a su forma original.
    
    Parámetros:
    - seudonimos (list): Lista de datos cifrados (seudonimizados).
    
    Retorna:
    - list: Lista de datos originales descifrados.
    """
    originales = [cifrador.decrypt(seudonimo.encode()).decode() for seudonimo in seudonimos]
    return originales

# ----------------------------------------------------------------------------------------
# -------------------------- EJEMPLO DE USO ----------------------------------------------
# ----------------------------------------------------------------------------------------

# Datos originales
nombres = ["Alex", "Ester", "Armando", "Javiera"]

print("=== Original ===")
print(nombres)

# Seudonimización reversible
nombres_seudonimizados = seudonimizar_datos_reversibles(nombres)
print("\n=== Seudonimización ===")
print(nombres_seudonimizados)

# Reversión de seudónimos
nombres_originales = revertir_seudonimos(nombres_seudonimizados)
print("\n=== Reversión de Seudonimización ===")
print(nombres_originales)

# Mostramos la clave utilizada para una mejor comprensión
print("\n=== Clave utilizada ===")
print(f"Clave secreta: {clave_secreta}\n")

""" En este ejercicio usamos Fernet.generate_key() para crear una clave única. 
    Es importante guardar esta clave en un lugar seguro, como un archivo protegido 
    o una base de datos segura. Si perdemos la clave, no podremos revertir los datos.
"""