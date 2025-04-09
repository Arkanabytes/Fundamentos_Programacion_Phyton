#Bucle While
contador = 1

while contador <=5:
    print ('Numero', contador)
    contador = contador +1 #Contador +1
    
print('---------------------------------')

#Bucle for con range()
for i in range (5):
    print ('Numero', i)

print('---------------------------------')
#Hace un programa que muestre todos los numeros anteriores desde el 1 hasta el numero de usuario()
numeroUsuario = int(input('Ingrese un numero'))
for i in range (1,numeroUsuario):
    print ('Usuario', i)
    
print('---------------------------------')
#Hace un programa que muestre todos los numeros anteriores desde el 1 hasta el numero de usuario()
numeroUsuario = int(input('Ingrese un numero'))
for i in range (1,numeroUsuario):
    print ('Listado', i)
    
print('---------------------------------')
nombre= input ('Ingrese su nombre: ')
for letra in nombre:
    print ('Letra')