# Actividades favoritas
#Problema:
# Pide al usuario que ingrese sus actividades favoritas (leer, correr, pintar, etc.). 
# Guarda cada actividad en una lista actividades. Detén el programa si escribe "fin", 
# y muestra los resultados.

actividadesFavoritas=[]
while True:
    nombre = input('Ingrese su actividad favorita o si no escriba fin: ')
    if nombre.lower() =='fin':
        break
    actividadesFavoritas.append(nombre)
print('\nEl listado de las actividades es: ')
for i, nombre in enumerate(actividadesFavoritas, start=1):
    print(f'{i}.{nombre}')
