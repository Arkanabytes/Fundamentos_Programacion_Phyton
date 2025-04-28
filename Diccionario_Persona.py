 # Persona
 # Problema:Crea un diccionario llamado persona. Pide nombre, edad y ciudad. Luego muestra:

persona= {}
persona['nombre'] = input('Ingrese su nombre completo: ')
persona['edad'] = int(input('Ingrese su edad: '))
persona['ciudad'] = input('Ingrese nombre ciudad de nacimiento: ')
persona['pais'] = input('Ingrese el pais donde nacio: ')

print(f"Mi nombres es {persona['nombre']} tengo {persona['edad']} y naci en la ciudad de {persona['ciudad']} en el pais de {persona['pais']} ")