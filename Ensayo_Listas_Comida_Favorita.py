# Cree un listado de su comida favorita
#Pedir al usuario 3 comidas favoritas, guardarlas en una lista y mostrarlas numeradas.

#Creo la lista
comidas= []

# Declaro mediante un for que me solicite tres veces la pregunta
for i in range(3):
    comida = input(f'Por favor ingrese sus comidas favoritas {i+1}: ') # declaro que ingrese las comidas pero que inicialice desde el 1

    # se ingresa la comida a la lista
    comidas.append(comida)


# Paso 3: Mostrar las comidas ingresadas con numeración
print('\n El listado de comidas es :')
for i, comida in enumerate(comidas, start = 1 ):
    print(f' {i}.{comida}')
