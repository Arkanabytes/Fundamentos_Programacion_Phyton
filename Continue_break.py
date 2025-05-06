# Usuario ingrese numero
# Si el numero es 0, numero no valid, que intente de nuevo y vuelva a pedir otro numero ( usa funcion continue) si el numero es 7,
# muestre secreto encontrado y detiene el bucle
# usando el break y en los dos casos muestra numero ingresado-

for i in range (1,100):
    num = int(input('Ingrese un numero del uno al 10: '))

    if num == 0:
        print ('Numero invalido, por favor intentalo otra vez')
        continue
    if num == 7:
        print ('El numero es valido Numero secreto encontrado !')
        break   
    print ('Numero ', num)
print ('Autor: Consuelo Pinto')
