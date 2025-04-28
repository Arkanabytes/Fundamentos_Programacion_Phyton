# Ejercicio 1: Lista de libros leídos
#Problema:
#Crea una lista vacía llamada libros. Pide al usuario que ingrese nombres de libros 
# que haya leído. El usuario debe poder ingresar tantos libros como quiera hasta que escriba 
# "fin". Finalmente, imprime la lista enumerada de libros.

libros = []
while True:
    libro = input('Ingrese el listado de libros: ')
    if libro.lower()=='fin':
        break
    libros.append(libro)
print('Ingrese el numero de variables')
for i, libros in enumerate(libro,star=1):
    print(f'{i}.{libros}')