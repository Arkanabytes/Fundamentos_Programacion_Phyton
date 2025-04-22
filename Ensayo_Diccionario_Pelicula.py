# Crea un diccionario llamado pelicula. Pide al usuario que ingrese el título, 
# director y año de estreno. Valida que el año sea un número mayor a 1900.

# Crea un diccionario 
pelicula = {}

pelicula ["Titulo"] = input ("Ingrese el titulo de la pelicula: ")
pelicula ["Director"] = input ("Ingrese el nombre del director de la pelicula: ")

while True:
    try:
        anio = int(input (" Ingrese el año del estreno: ")) # pedimos el año
        if anio > 1900: # si el año es mayor al 1900, lo guardamos
            pelicula['anio'] = anio
            break
        else: # Si el año no es valido mostrasmos un mensaje
            print('Por favor ingrese un año superior al 1900.')
            # En caso de error en la tipificacion debe ingresar un numero valido.
    except ValueError:
        print("Error: debe ingresar un número válido.")
# Paso 4: Mostrar la informacion recopilada 
print(f'\n La pelicula {pelicula["Titulo"]} fue dirigida {pelicula["Director"]} en {pelicula["anio"]}')