# Crear el diccionario 
productos = {}

# Bucle infinito para ingresar productos
while True:
    nombre = input('Nombre de producto (o "salir" para terminar): ')
    if nombre.lower() == 'salir':
        break
    try:
        precio = int(input('Precio: '))
        stock = int(input('Stock: '))
        
        productos[nombre] = {
            'precio': precio,
            'stock': stock
        }
    except ValueError:
        print("Por favor ingresa números válidos para precio y stock.")
        continue

# Mostrar productos ingresados
print('\nProductos Ingresados:')
for nombre, datos in productos.items():
    print(f'El producto "{nombre}" cuesta ${datos["precio"]} y quedan {datos["stock"]} unidades.')