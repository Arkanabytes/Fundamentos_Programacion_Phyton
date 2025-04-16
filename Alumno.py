# Crear un diccionario llamado alumno
# Nombre, edad, carrera.
# 'Juan tiene 18 años y estudia derecho'

# Diccionarios

alumno ={ 'nombre': ' Juan', 'edad': 18}
print (alumno['nombre']) # Juan
print (alumno)
alumno = {
    'nombre': 'Juan',
    'edad': 18,
    'carrera': 'Derecho'
}
print(alumno)
print(f'{alumno ['nombre']} tiene{alumno['edad']} años y estudia {alumno['carrera']}' )

print('-------------------------------------------------------------------')

alumnos = {
    '12345678-9' : {
        'nombre': 'Juan',
        'edad': 20,
        'carrera': 'ingenieria'
    },
     '98765432-1' : {
        'nombre': 'Juan',
        'edad': 18,
        'carrera': 'ingenieria'
}
}

# Acceder a alumno especifico
print(alumnos['12345678-9']['nombre'])

#recorrer diccionario

for rut,datos in alumnos.items():
    print(f'Rut: {rut}')
    print(f'Nombre {datos['nombre']}')
    print(f'Edad {datos['edad']}')
    print(f'Carrera {datos['carrera']}')
    