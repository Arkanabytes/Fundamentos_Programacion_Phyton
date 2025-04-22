# Lista de animales
#Pedir al usuario 4 animales y mostrarlos luego numerados.

#Creo lista
animales = []

# Creo un for con el rango cuatro para que me lo solicites 4 veces
for i in range(4):
    animal = input(f'Ingrese el numero de los tres animales favoritos {i+1}: ')
    animales.append(animal)

# Solicito el numero de listado a traves de un print 
print ('\n El numero de listado de animales favoritos es :' )
for i, animal in enumerate(animales,start=1):
    print(f' {i}.{animal}')



