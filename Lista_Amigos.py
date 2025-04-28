# Lista de amigos
#Problema:
#Solicita nombres de amigos para agregarlos a una lista llamada amigos. 
# Usa un bucle que se detenga cuando se escriba "fin". Luego imprime todos 
# los nombres con su número correspondiente.

amigos = []
while True:
    nombre = input('Ingrese un listado de amigos o si no escriba Fin: ')
    if nombre.lower()=='fin':
        break
    amigos.append(nombre)
print('El listado de amigos es: ')
for i, nombre in enumerate(amigos, start=1):
        print(f'{i}. {nombre} ')

