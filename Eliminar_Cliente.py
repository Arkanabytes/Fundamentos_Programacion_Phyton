def eliminardatos():
    print("===================================")
    print("      MODULO ELIMINAR CLIENTE      ")
    print("===================================")
    mostrartodo()
    try:
        elim = int(input("Ingrese valor de ID del Cliente que desea Eliminar: "))
    except ValueError:
        print("Error: Debe ingresar un número entero.")
        return

    if elim not in clientes:
        print("Error: ID no existe en la base de datos.")
        return

    confirmar = input(f"¿Está seguro que desea eliminar al cliente con ID {elim}? [SI/NO]: ")
    if confirmar.lower() == "si":
        del clientes[elim]
        print(f"Cliente con ID {elim} eliminado correctamente.")
    else:
        print("Eliminación cancelada.")

#Mejoras aplicadas:
#Validación del tipo de entrada (int).
#Verificación de existencia del ID en clientes.
#Confirmación antes de eliminar.
#Mensajes claros al usuario.

