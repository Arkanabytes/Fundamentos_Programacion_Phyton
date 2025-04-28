# Frutas favoritas
# Problema:
# Crea una lista vacía llamada frutas. Pide al usuario que ingrese sus 5 frutas favoritas y guárdalas en la lista. 
# Luego, muestra la lista numerada.

frutas=[]
for i in range(4):
    nombre = input(f'Ingresa tu fruta favorita {i+1}: ') 
    frutas.append(nombre)

print('\n El listado de la fruta es: ')
for i, nombre in enumerate(frutas,start= 1):
    print(f'{i}.{nombre}')