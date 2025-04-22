# Paso 1: Crear un diccionario vacío para almacenar la información
libro = {}

# Paso 2: Pedir el título y autor del libro al usuario
libro["titulo"] = input("Ingrese el título del libro: ")
libro["autor"] = input("Ingrese el autor del libro: ")

# Paso 3: Validar que el año de publicación sea mayor a 1900
while True:
    try:
        anio = int(input("Ingrese el año de publicación: "))  # Pedimos el año de publicación
        if anio > 1900:  # Si el año es mayor que 1900, lo guardamos
            libro["anio"] = anio
            break
        else:  # Si el año es menor o igual a 1900, pedimos que lo ingrese de nuevo
            print("Por favor, ingrese un año mayor a 1900.")
    except ValueError:  # Si el usuario ingresa un valor no numérico, mostramos un mensaje de error
        print("Error: debe ingresar un número válido.")
        
# Paso 4: Mostrar la información recopilada
print(f"\nEl libro '{libro['titulo']}' fue escrito por {libro['autor']} en {libro['anio']}.")


