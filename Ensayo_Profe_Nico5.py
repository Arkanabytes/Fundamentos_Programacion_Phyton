#  Lista de películas favoritas
# Pide al usuario que ingrese 3 películas favoritas y muéstralas al final en orden con numeración.

#compras = []
#for i in range(3):
 #   compra = input (f'Lista de la compra {i + 1}: ')
  #  compras.append(compra)
 #   break
#print ('\nTus peliculas favoritas son: ') 
#for i, compra in enumerate(compras, start= 1):
   # print(f'{i}.{compra}')
    
    
    
# Listas
compras =[]

while True:
    producto= input('Ingrese su nombre o escriba "Fin" para salir ')
    if producto.lower() == 'fin':
        break
    compras.append(producto)
print('Lista de nombres ingresados')
for i, producto in enumerate(compras, start=1):
    print(f'{i}.{producto}')
