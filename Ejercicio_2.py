# Ejercicio 2: Listas
# 1-.Cree un programa en Python que permita al usuario ingresar productos para una lista de compras.
# 2-.Utilice un bucle while para solicitar los nombres de los productos uno a uno y almacénelos en una
# lista llamada compras.
# 3-.El ingreso de productos debe finalizar cuando el usuario escriba la palabra “fin”.
# Al finalizar, muestre por pantalla el contenido de la lista numerada con este formato:

compras= []
while True:
    productos= input('Ingrese una de lista de compras y para finalizar escriba Fin: ')
    if productos.lower() == 'fin':
        break
    compras.append(productos)
print ('\n El listado de la compra es: ')
for i, productos in enumerate(compras, start=1):
    print(f'{i}.{productos}')
    

print('\nAutor: Consuelo Pinto')