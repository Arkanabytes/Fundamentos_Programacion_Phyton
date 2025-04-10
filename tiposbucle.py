
contador = 1

while contador <= 5:
    print (f'Numero: {contador}')# print (numero, contador)
    contador+=1
    
    
# for recorre la secuencia
print ('-------------------------------------')
for numero in range (1,6):
    print ( f'Numeros: {numero}')

# Ejercicio
# Ingrese un numero e imprima desde uno hasta el numero que de el usuario

limite= int (input('Ingrese un numero'))
contador = 1

while contador <= limite:
    print (contador)
    contador+= 1 # contador +1 
    
# bucle infinit

while True:
    nombre = input ('Escribe tu nombre: ')
    print(f'Hola {nombre}')