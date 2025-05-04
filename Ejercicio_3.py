# Ejercicio 3: Diccionario
# Cree un programa en Python que solicite al usuario ingresar sus datos personales: nombre, edad y
# pasatiempo.
# Almacene esta información en un diccionario llamado persona.
# Convierta la edad a tipo entero (int).
# Luego, utilice un bucle for para mostrar los datos, uno por línea, con este formato:

persona = {}
persona['nombre'] = input('\nIngrese su nombre: ')
persona['edad'] = int(input('\nIngrese su edad: '))
persona['pasatiempo'] = input('\nIngrese su pasatiempo: ')

print("\nDatos ingresados:")
for clave, valor in persona.items():
    print(f"{clave.capitalize()}: {valor}")

print('\nAutor: Consuelo Pinto')
