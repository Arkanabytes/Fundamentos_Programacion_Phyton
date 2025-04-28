#crea diccionario llamado videojuego
#solicite al usuario nombre video juego,empresadesarrolladora y año de video juego
#el videojuego" fue desarrolado por" "el año"

video_juego={}

video_juego['nombre']=input('ingrese el nombre del video juego')
video_juego['empresadesarrolladora']=input('ingrese la empresadesarrolladora')
video_juego['anio']=int(input('ingrese el año del video juego'))

print(f"El video juego {video_juego['nombre']} fue desarrolado por{video_juego['empresadesarrolladora']} y el año{video_juego['anio']}")
