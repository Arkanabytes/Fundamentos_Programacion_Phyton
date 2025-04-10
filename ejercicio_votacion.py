# Ejercicio de votaciones
edad =  int(input ('Cual es tu edad? '))
edad_votacion = 18

if edad < 18:
    print (' Eres menor de edad, no puedes votar ')
elif edad == 18:
    print (' Justo tienes 18 años, si puedes votar')
if edad < edad_votacion:
    años_faltantes = edad_votacion - edad
print(f'Te falta :  {años_faltantes}' )

#else:
 #   print (' Eres mayor de edad')