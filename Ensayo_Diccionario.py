# Crear un diccionario vacío para guardar información del libro
libro = {}

# Solicitar al usuario el título del libro y guardarlo en el diccionario
libro["titulo"] = input("Ingrese el título del libro: ")

# Solicitar el autor del libro y guardarlo
libro["autor"] = input("Ingrese el autor del libro: ")

# Solicitar el año de publicación y convertirlo a entero
libro["anio"] = int(input("Ingrese el año de publicación: "))

# Mostrar el mensaje con los datos ingresados
print(f"\nEl libro '{libro['titulo']}' fue escrito por {libro['autor']} en {libro['anio']}.")