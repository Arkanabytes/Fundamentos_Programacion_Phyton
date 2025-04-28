# Comidas preferidas
#Problema:
#Permite al usuario guardar sus comidas preferidas en una lista llamada comidas. Debe escribir "fin" p
# ara dejar de ingresar datos. Luego, imprime la lista con numeración.

comidas = []
while True:
    nombre = input('Ingrese el listado de comidas preferidas o escriba salir: ')
    if nombre.lower() == 'fin':
        break
    comidas.append(nombre)
print('\n El listado de comida es: ')
for i, nombre in enumerate(comidas, start=1):
    print(f'{i}.{nombre}')