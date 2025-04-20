#Escribe un programa para registrar libros en una biblioteca. Por cada libro, se debe ingresar 
# el título, el autor y la cantidad de copias disponibles. La entrada finaliza cuando se ingresa 
# "salir" como título. Al terminar, muestra un resumen con los datos de cada libro registrado.

#Listas

registro_libro ={}
while True:
    nombre_libro = input( 'Nombre del libro, autor y cantidad de copias o escribir salir : ')
    if nombre_libro.lower() == 'salir':
        break
    libro = input(' Titulo libro: ')
    autor = input(' Nombre del autor: ')
    cantidad = int (input(' Cantidad de copias: '))

    registro_libro[nombre_libro] ={
        ' Titulo libro: ' : libro,
        ' Nombre del autor' : autor,
        ' Cantidad de copias': cantidad
    }
print('\n Libros registrados')
for nombre_libro in registro_libro.items():
    print(f'{nombre_libro} el autor es: {autor} y el numero de copias es {cantidad}  ')