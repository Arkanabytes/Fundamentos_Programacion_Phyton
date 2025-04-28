#Metas del año
#Problema:
#Haz que el usuario escriba sus metas para este año. Guarda cada meta en la lista metas. El usuario puede 
# escribir tantas como quiera hasta escribir "fin". Imprime las metas con número.

metas = []
while True:
    nombre = input('Ingrese sus metas del anio o si no escriba FIN: ')
    if nombre.lower() == 'fin':
        break
    metas.append(nombre)
print('\n El listado de las metas ')
for i, nombre in enumerate(metas, start=1):
    print(f'{i}.{nombre}')