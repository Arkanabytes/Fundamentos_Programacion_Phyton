# Diccionarios

persona ={ 'nombre': 'Ana', 'edad': 30}
print (persona['nombre']) # Ana
print (persona)
persona = {
    'nombre': 'ana',
    'edad': 30,
    'ciudad': 'santiago'
}

# Crear diccionario desde cero
print (persona['nombre'])
print (persona['ciudad'])

producto= {} #Producto vacio
producto ['nombre'] = 'Mouse'
producto ['precio'] = 12000
producto ['stock'] = 25

print(producto)

for clave in producto:
    print(clave, '->', producto [clave])
    
# Modificar agregar y eliminar datos
producto['stock'] = 30 # modificar
producto['categoria'] = 'periferico' #agregar
del producto ['precio'] #eliminar
print ('----------------------')
print(producto)