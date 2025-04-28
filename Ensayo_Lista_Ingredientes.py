# Crea una lista vacía llamada ingredientes
# El usuario puede ingresar ingredientes para una receta hasta escribir 'fin'
# Al final, se imprimen todos los ingredientes numerados

ingredientes = []
while True:
    ingrediente =input('Agregue los ingredientes o escriba fin para terminar: ')
    if ingrediente.lower() == 'fin':
        break
    ingredientes.append(ingrediente)
print('\n El listado de ingredientes es: ')
for i, ingrediente in enumerate(ingredientes, start=1):
    print(f"{i}.{ingrediente}")