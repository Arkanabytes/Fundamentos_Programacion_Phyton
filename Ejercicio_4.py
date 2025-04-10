# Ejercicio con listas
# 1.- Pedir al usuario que ingreso 3 comidas
# 2.- Guardar en una lista
# 3.- Imprima una por una

# Paso 1 crear una lista
comidas= []

# Paso 2: Ingresar las 3 comidas
for i in range(4):
    comida=input(f'Ingrese su comida favorita n{i+1}: ')
    comidas.append(comida)
    
# Paso 3.- Mostrar comidas una por una
print ('\n Tus comidas favoritas son: ')
for comida in comidas:
    print('-'+ comida) 