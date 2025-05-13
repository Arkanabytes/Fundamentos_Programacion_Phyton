#Crea una lista
# Preguntar al usuario por 3 pasatiempos o hobbies y mostrarlos.

#Creo un lista
pasatiempos = []
for i in range(3):
    pasatiempo = input(f'Ingrese tres pasatiempos favoritos {i+1}: ')
    pasatiempos.append(pasatiempo)
# Solicito el numero de listado a traves de un print 
print('\n El listado de los hobbies es: ' )
for i, pasatiempo in enumerate(pasatiempos, start= 1):
    print(f'{i}.{pasatiempo}')
