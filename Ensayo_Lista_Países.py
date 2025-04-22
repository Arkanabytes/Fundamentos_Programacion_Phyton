#Lista de países
#Pide al usuario que ingrese 5 países que le gustaría visitar. Guárdalos en una lista y muéstralos 
# al final con numeración.

paises = []

for i in range(5):
    pais = input(f'Ingrese los cincio paises que le gustaria visitar {i+1}: ')
    paises.append(pais)

print ('\n Paises que desea visitar: ')
for i, pais in enumerate(paises,start=1):
    print (f' {i}.{pais}')