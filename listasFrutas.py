# Listas
frutas=['Manzana', 'Pera','Mango']

# indice pare en 0 y cada valor recibe el primer elemento

# acceder a los elementos
print(frutas)
print (frutas[0]) # Manzana
print (frutas[2]) # Pera

# modificar elementos de la lista
frutas [1] = 'kiwi'
print(frutas) # manzana, kiwi, mango

# metodos utiles para modificar una lista
frutas.append('Uva') # agrega
print(frutas) # ['Manzana', 'Pera','Mango', 'Uva']

frutas.remove('Manzana') # agrega
print(frutas) # ['kiwi', 'Pera', 'Uva']

print(len(frutas))# cantidad de elementos
frutas.sort() #ordenar alfabeticamente
print(frutas)

# recorre una lista con un for

for fruta in frutas:
    print(f'Me gusta la {fruta}')