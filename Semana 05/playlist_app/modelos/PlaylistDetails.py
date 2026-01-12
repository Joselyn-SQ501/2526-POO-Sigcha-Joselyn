# Subclase para ingresar datos sobre la playlist
class PlaylistDetails:
    # Creación de un constructor vacío
    def __init__(self):
        self.name = ""   # Atributo para ingresar el nombre de la playlist como tipo de dato string.
        self.total_songs = 0  # Atributo para ingresar el número total de canciones de la playlist como tipo de dato integer.
        self.average_duration_music = 0.0   # Atributo para ingresar la duración promedio de las canciones de la playlist como tipo de dato float.
        self.media_format = "" # Atributo para ingresar el formato de las canciones de la playlist como tipo de dato string.

    # Método para solicitar los datos sobre la playlist al usuario
    def enter_details(self):
        self.name = input('Ingresa el nombre de la playlist: ')
        self.total_songs = int(input('Ingrese el total de canciones que tiene la playlist: '))
        self.average_duration_music = float(input('Ingresa la duración promedio de las canciones (en minutos): '))
        self.media_format = input('¿En qué formato escucha esta playlist? (mp4 o mp3): ')