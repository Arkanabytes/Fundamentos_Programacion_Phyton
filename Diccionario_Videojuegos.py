#Videojuego
#Problema:Crea un diccionario llamado video_juego. Solicita al usuario el nombre del videojuego, la empresa 
# desarrolladora y el año en que fue lanzado. Muestra el mensaje:

videojuego = {}
videojuego['nombre'] = input('Ingrese el nombre del videojuego: ')
videojuego['empresa'] = input('Ingrese el nombre de las empresa del videojuego: ')
videojuego['anio'] = int(input('Ingrese el año del videojuego: '))
print(f"El videojuego se llama: {videojuego['nombre']}y fue fabricado por {videojuego['empresa']} en el anio {videojuego['anio']} ")