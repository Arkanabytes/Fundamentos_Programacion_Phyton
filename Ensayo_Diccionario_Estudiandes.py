# Datos de un estudiante
# Paso 1: Crear un diccionario vacio para almacenar la informacion
estudiante = {}

# Paso 2: 
estudiante["nombre"] = input("Ingrese el nombre del estuduiante: ")
estudiante["carrera"] = input("Ingrease la carrera del estudiante: ")

while True:
    try:
        anio = int(int(input("Ingrese el año de ingreso: ")))
        if anio > 2000:
            estudiante ["anio_ingreso"]= anio
            break
        else:
            print("Por favor, ingrese un año mayo al 2000 ")
    except ValueError:  # Si el usuario ingresa un valor no numérico, mostramos un mensaje de error
        print("Error: debe ingresar un número válido.")

print(f"\n El estudiante '{estudiante['nombre']}' {estudiante['carrera']} {estudiante['anio_ingreso']}")