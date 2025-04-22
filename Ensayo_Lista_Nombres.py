# Lista de nombres
#Solicita al usuario que ingrese 3 nombres de personas. Almacena cada uno en una lista llamada 
# nombres y luego imprímelos numerados.

nombres = []
for i in range(3):
    nombre = input(f' Ingrese el nombre de tres personas: {i +1}')
    nombres.append(nombre)

print ("\n Nombres ingresados: ")
for i, nombre in enumerate(nombres,start=1): 
    print(f' {i}.{nombre}')