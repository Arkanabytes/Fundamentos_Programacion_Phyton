#  Lista de películas favoritas
# Pide al usuario que ingrese 3 películas favoritas y muéstralas al final en orden con numeración.

peliculas = []
for i in range(3):
    pelicula = input (f'Ingrese sus tres peliculas favoritas {i + 1}: ')
    peliculas.append(pelicula)

print ('\nTus peliculas favoritas son: ') 
for i, pelicula in enumerate(peliculas, start= 1):
    print(f'{i}.{pelicula}')
