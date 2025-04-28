#  Películas por ver
#Problema:
#Crea una lista llamada peliculas. El usuario debe ingresar títulos de películas que quiere ver. 
# Usa un bucle while para seguir pidiendo títulos hasta que escriba "fin". Muestra la lista numerada.

peliculas = []

while True:
    pelicula = input('Agrega una película a tu lista (o escribe "fin"): ')
    if pelicula.lower() == 'fin':
        break
    peliculas.append(pelicula)

print('\nPelículas para ver:')
for i, pelicula in enumerate(peliculas, start=1):
    print(f'{i}. {pelicula}')