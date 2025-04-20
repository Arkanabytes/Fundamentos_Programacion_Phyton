
#Ejercicio 2: Inventario de empleados
empleados = {}

while True:
    nombre = input('Nombre del empleado (o "salir" para terminar): ')
    if nombre == 'salir':
        break
    cargo = input('Cargo: ')
    sueldo = int(input('Sueldo mensual: '))

    empleados[nombre] = {
        'cargo': cargo,
        'sueldo': sueldo
    }

print('\nEmpleados Registrados:')
for nombre, datos in empleados.items():
    print(f'{nombre} trabaja como {datos["cargo"]} y gana ${datos["sueldo"]}')
