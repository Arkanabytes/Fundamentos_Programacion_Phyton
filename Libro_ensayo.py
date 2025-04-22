#Crea	un	diccionario	llamado	`libro`.	Pide	al	usuario	que	ingrese:	título,	autor	y	año	
#de	publicación.	Valida	que	el	año	ingresado	sea	un	número	entero	positivo mayor	a	
#1900.	Muestra	la	información	así:
#'El	libro	'Cien	Años	de	Soledad'	fue	escrito	por	Gabriel	García	Márquez	en	1967.'

libro = {}
    libro["titulo"] = input("Ingrese el título del libro: ")
    libro["autor"] = input("Ingrese el autor del libro: ")
    while True:
        try:
            anio = int(input("Ingrese el año de publicación: "))
            if anio > 1900:
                libro["anio"] = anio
                break
        else:
            print("Por favor, ingrese un número positivo.")
        except ValueError:
        print("Error: debe ingresar un número válido.")
print(f"\nEl libro '{libro['titulo']}' fue escrito por {libro['autor']} en {libro['anio']}.")