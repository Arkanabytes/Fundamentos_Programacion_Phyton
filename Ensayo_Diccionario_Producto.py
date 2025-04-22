# Paso 1: Crear un diccionario vacío para almacenar la información
producto = {}

# Paso 2: Pedir el nombre del producto y la categoría al usuario
producto["nombre"] = input("Ingrese el nombre del producto: ")
producto["categoria"] = input("Ingrese la categoría del producto: ")

# Paso 3: Validar que el precio sea un número mayor a 0
while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))  # Pedimos el precio
        if precio > 0:  # Si el precio es mayor a 0, lo guardamos
            producto["precio"] = precio
            break
        else:  # Si el precio es menor o igual a 0, pedimos que lo ingrese de nuevo
            print("El precio debe ser mayor a 0.")
    except ValueError:  # Si el usuario ingresa un valor no numérico, mostramos un mensaje de error
        print("Error: debe ingresar un número válido.")
        
# Paso 4: Mostrar la información recopilada
print(f"\nEl producto '{producto['nombre']}' pertenece a la categoría '{producto['categoria']}' y cuesta ${producto['precio']}.")
