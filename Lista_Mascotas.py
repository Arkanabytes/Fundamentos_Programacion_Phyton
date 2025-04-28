# Mascotas
#Problema:
#Haz un programa que pida los nombres de las mascotas del usuario. Guarda los nombres en una lista mascotas 
# y muestra la lista numerada cuando escriba "fin".

mascotas = []
while True:
    nombre = input('Ingrese el listado de las mascotas o si no escriba fin: ')
    if nombre.lower() =='fin':
        break
    mascotas.append(nombre)
print('El listado de mascostas es: ')
for i, nombre in enumerate(mascotas, start=1):
    print(f'{i}.{nombre}')