def ingresoUsuarios():
    print("=======================================")
    print("        INGRESO DE USUARIO             ")
    print("=======================================")
    
    username = input("INGRESE NOMBRE DE USUARIO: ").strip()
    if not username:
        print("Error: El nombre de usuario no puede estar vacío.")
        return
    if username in usuarios:
        print("Error: El usuario ya existe.")
        return

    clave = input("INGRESE PASSWORD: ").strip()
    if len(clave) < 4:
        print("Error: La contraseña debe tener al menos 4 caracteres.")
        return

    nombre = input("INGRESE NOMBRE: ").strip()
    apellidos = input("INGRESE APELLIDOS: ").strip()
    correo = input("INGRESE CORREO: ").strip()
    
    if "@" not in correo or "." not in correo:
        print("Error: Correo inválido.")
        return

    global idusuario
    idusuario += 1
    codigo = idusuario
    usuario = [codigo, username, clave, nombre, apellidos, correo]
    usuarios[username] = usuario

    print(f"Usuario {username} registrado correctamente con ID {codigo}.")
