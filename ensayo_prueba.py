# Ejercicio 1
# While y diccionario de datos
# diccionario productos
# usuario debe agregar productos (while)
# cuando el usuario termine de agregar productos escriba 'salir' y salga
# utiliza for para mostrar los productos

# crear el diccionario 
productos = {}

# buchle infinito
while True:
    nombre = input('Nombre de producto (o "salir" para terminar): ')
    if nombre == 'salir':
        break
    precio= int(input('Precio: '))
    stock = int (input ('Stock: '))
    
    productos[nombre] = {
        'precio': precio,
        'stock' : stock
}

print ('Productos Ingresados')
for nombre, datos in productos.items():
    print(f'El producto {nombre} cuesta $ {datos[precio]} y quedan {datos[precio]} y quedan {datos[stock]} unidades ')