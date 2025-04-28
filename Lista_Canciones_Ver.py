# Canciones favoritas
#Problema:
#Pide al usuario que ingrese sus canciones favoritas. Guarda cada una en una 
# lista llamada canciones. Cuando escriba "fin", termina y muestra las canciones enumeradas.

canciones = []

while True:
    cancion = input('Canción favorita (o "fin" para salir): ')
    if cancion.lower() == 'fin':
        break
    canciones.append(cancion)

print('\nTus canciones favoritas:')
for i, cancion in enumerate(canciones, start=1):
    print(f'{i}. {cancion}')