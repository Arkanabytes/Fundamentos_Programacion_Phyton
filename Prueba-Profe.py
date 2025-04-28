tareas = []

while True:
    tarea = input(f'Ingrese las tareas que tiene: ')
    if tarea.lower() == 'fin':
        break
    tareas.append(tarea)
print('\n Tareas Ingresadas: ')
for i, tarea in enumerate(tareas, start=1):
    print(f'{i}.{tarea}')