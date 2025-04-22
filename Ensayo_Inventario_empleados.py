#Problema:
#Haz un programa que permita llevar un registro de empleados. 
#Se debe pedir el nombre del empleado, el cargo que ocupa y su sueldo 
#mensual. El programa termina cuando se escribe "salir" como nombre. 
#Al final, se debe imprimir la información de cada empleado registrado.

# Listas
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
