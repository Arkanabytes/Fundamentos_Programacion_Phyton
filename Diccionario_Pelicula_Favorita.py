# Película favorita
# Problema:
# Crea un diccionario llamado pelicula. Pide al usuario el nombre de su película favorita, el director y el 
# año de estreno. Luego, imprime un mensaje que diga:

peliculaFavorita={}
peliculaFavorita['nombre']= input('Ingrese el nombre de la pelicula favorita: ')
peliculaFavorita['director']= input('Ingrese el nombre del director: ')
peliculaFavorita['anio_estreno']= int(input('El anio de estreno: '))

print(f"Su pelicula favorita es: {peliculaFavorita['nombre']} el nombre del director es {peliculaFavorita['director']} y se estreno en el anio {peliculaFavorita['anio_estreno']}")
