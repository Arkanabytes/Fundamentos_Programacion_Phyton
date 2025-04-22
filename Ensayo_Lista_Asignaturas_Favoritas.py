# Crea una lista de tus tres asignaturas favoritas

asignaturas = []
for i in range(3):
    asignatura = input(f' Ingrese sus tres asignaturas favoritas {i+1}: ')
    asignaturas.append(asignatura)
print('\nSus asignaturas favoritas son : ')
for i, asignatura in enumerate(asignaturas, start=1):
    print(f'{i}.{asignatura}')


print('\nAutor: Consuelo Pinto')