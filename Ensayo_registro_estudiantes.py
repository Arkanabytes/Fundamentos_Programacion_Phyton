#Problema:
#Crea un programa en Python que permita registrar estudiantes. El programa 
# debe pedir al usuario el nombre del estudiante, su nota final y su edad. 
# La entrada de datos debe continuar hasta que se escriba la palabra "salir". 
# Luego, muestra una lista con todos los estudiantes registrados, su edad y 
# su nota final.

# Lista

estudiantes={}
while True:
    nombre= input('Ingrese nombre del estudiante para su registro o escriba "Salir": ')
    if nombre.lower() == 'salir':
        break
    nombre_e = input ('Nombre: ')
    nota = int (input ('Nota del alumno: '))
    edad = int (input ('Edad: '))
        
    estudiantes[nombre]={
            'Nombre' : nombre_e,
            'Nota del Alumno' : nota,
            'Edad': edad
        }
    print('\n Estudiantes registrados: ')
    for nombre in estudiantes.items():
        print(f'{nombre_e} nota del alumno es: {nota} y la edad del alumno es {edad}')

