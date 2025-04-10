
        
    #Menu con while True

while True:
    print('\n Menú:')
    print('1-. Saludar')
    print('2-. Pregunta edad')
    print('3-. Salir')

    opcion=input('Elige una opcion 1/2/3:')

    if opcion == '1':
        print( 'Holaaaa!!!')
    elif opcion == '2':
        edad=int(input('¿Cual es tu edad?'))
        print (f'Tienes {edad} años')
    elif opcion == '3':
        print ('Hasta luego, chao')
        break
    else:
        print('Opcion no válida, intente de nuevo')