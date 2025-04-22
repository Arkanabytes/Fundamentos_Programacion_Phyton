# Crea una lista vacia que se llame nombres
# Permite al usuario ingresar nombre en bucle while hasta que escriba fin, luego 
# agrega cada nombre a la lista e imprimelos (numerados) usando el bucle for

# Listas
nombres =[]

while True:
    nombre= input('Ingrese su nombre o escriba "Fin" para salir ')
    if nombre.lower() == 'fin':
        break
    nombres.append(nombre)
print('Lista de nombres ingresados')
for i, nombre in enumerate(nombres, start=1):
    print(f'{i}-.{nombre}')