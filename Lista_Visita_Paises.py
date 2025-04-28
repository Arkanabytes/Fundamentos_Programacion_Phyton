# Países que deseas visitar
#Problema:
#Crea un programa que permita al usuario ingresar los países que quiere visitar y guardarlos 
# en una lista paises. Termina cuando escriba "fin" y muestra todos los países con su número.

paises= []
while True:
    nombre = input('Ingrese el nombre del pais que desea visitar o si no escriba salir: ')
    if nombre.lower() == 'fin':
        break
    paises.append(nombre)
print('El listado de paises es: ')
for i, nombre in enumerate(paises, start=1):
    print(f'{i}.{nombre}')
