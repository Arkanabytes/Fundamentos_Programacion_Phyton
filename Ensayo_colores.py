# Crea	una	lista	vacía	llamada	`colores`.
# Pide	al	usuario	que	ingrese	3	colores.	Guarda	

colores = []
for i in range(3):
 color = input(f"Ingrese el color {i + 1}: ")
 colores.append(color)
print("\nColores ingresados:")
for i, color in enumerate(colores, start=1):
 print(f"{i}. {color}")