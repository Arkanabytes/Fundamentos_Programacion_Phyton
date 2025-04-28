# Videojuegos favoritos
# Problema:
# Crea un programa donde el usuario pueda ingresar sus videojuegos favoritos en una lista videojuegos. Cuando 
# escriba "fin", muestra todos los videojuegos con su número.

videojuegos= []
while True:
    nombre= input('Ingrese el videojuego favorito o si no escriba fin: ')
    if nombre.lower() =='fin':
        break
    videojuegos.append(nombre)

print('\n El listado de videojuegos')
for i, nombre in enumerate(videojuegos, start=1):
    print(f'{i}.{nombre}')