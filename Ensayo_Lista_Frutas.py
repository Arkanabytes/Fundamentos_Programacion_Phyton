# Lista de frutas
# Pide al usuario que ingrese 4 frutas y almacénalas en una lista llamada frutas. Luego imprime 
# la lista con numeración.

frutas = []
for i in range(4):
    fruta = input(f'Ingrese el nombre de la fruta {i + 1}: ')
    frutas.append(fruta)

    print ('\n Frutas ingresadas: ')
for i, fruta in enumerate (frutas, start=1):
        print(f'{i}.{fruta}')