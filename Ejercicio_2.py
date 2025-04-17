# Crear un programa que:
# Permita agregar dos alumnos desde el teclado (input)
# guarde los datos de un diccionario
# Imprima todos los alumnos

alumnos ={}
# repetir 2 veces para ingresar dos veces
for i in range(2):
    print(f'\n Registro del primer alumno {i+1}')
    rut= input('Ingrese el Rut del alumno: ')
    nombre= input('Ingrese el nombre: ')
    edad= int (input('Ingrese su edad'))
    carrera = input('Ingrese carrera: ')
    
    alumnos[rut] ={
            'nombre': nombre,
            'edad': edad,
            'carrera': carrera
    }
    # mostrar todos los alumnos registrados
    print ('Listas de alumnos')
    for i,(rut, datos) in enumerate(alumnos.items(), start = 1):
        print(f'Alumno: {i}')
        print(f'Rut {rut}')
        print(f'Nombre {datos['nombre']}')
        print(f'Edad {datos['edad']}')
        print(f'Carrera {datos['carrera']}')