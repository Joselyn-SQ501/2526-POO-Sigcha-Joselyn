# Subclase para ingresar datos sobre los hábitos de escucha de la playlist
class ListeningHabits:
    # Creación de un constructor vacío
    def __init__(self):
        self.plays = 0  # Atributo para ingresar el número de reproducciones que ha hecho el usuario de la playlist como tipo de dato integer.
        self.likes = False  # Atributo para validar si la playlist recibió un me gusta por parte del usuario como tipo de dato booleano.
        self.comments = False # Atributo para validar si la playlist fue comentada por parte del usuario como tipo de dato booleano.
        self.shares = False # Atributo para validar si la playlist fue compartida por parte del usuario como tipo de dato booleano.
        self.creator = False # Atributo para validar si la playlist fue creada por el usuario como tipo de dato booleano.

    # Método para solicitar el número de reproducciones de la playlist al usuario
    def enter_playlist(self):
        self.plays = int(input('¿Cuántas veces has escuchado la playlist?: '))

        # Llamada a las funciones utilizadas
        self.changeLike()
        self.changeComments()
        self.changeShares()
        self.changeCreator()

    # Método para solicitar el cambio del estado del me gusta en la playlist
    def changeLike(self):
        # Inicio de un bucle while para obtener la confirmación o negación del usuario sobre el like a la playlist.
        while True:
            request = input('\n¿Dio like a esta playlist? (si/no): ').strip().lower() #Solicita al usuario confirmar o negar el like en la playlist quitando elementos innecesarios por medio de strip y normalizando el ingreso de dato.
            if request in ['si', 'sí', 'Si', 'Sí']:
                self.likes = True
                break #Cierra el bucle
            elif request == 'no':
                self.likes = False
                break #Cierra el bucle
            else:
                print("Por favor, responda 'si' o 'no'")  # Pide ingresar el dato de la forma solicitada, en caso de que el usuario ingrese un dato incorrecto.

    # Método para solicitar el cambio del estado del comentario en la playlist
    def changeComments(self):
        # Inicio de un bucle while para obtener la confirmación o negación del usuario sobre el comantario a la playlist.
        while True:
            request = input('¿Comentó esta playlist? (si/no): ').strip().lower() #Solicita al usuario confirmar o negar el comentario en la playlist quitando elementos innecesarios por medio de strip y normalizando el ingreso de dato.
            if request in ['si', 'sí', 'Si', 'Sí']:
                self.comments = True
                break #Cierra el bucle
            elif request == 'no':
                self.comments = False
                break #Cierra el bucle
            else:
                print("Por favor, responda 'si' o 'no'")  # Pide ingresar el dato de la forma solicitada, en caso de que el usuario ingrese un dato incorrecto.

    # Método para solicitar el cambio del estado de compartir de la playlist
    def changeShares(self):
        # Inicio de un bucle while para obtener la confirmación o negación del usuario sobre la compartición de la playlist.
        while True:
            request = input('¿Compartió esta playlist? (si/no): ').strip().lower() #Solicita al usuario confirmar o negar la compartición de la playlist quitando elementos innecesarios por medio de strip y normalizando el ingreso de dato.
            if request in ['si', 'sí', 'Si', 'Sí']:
                self.shares = True
                break #Cierra el bucle
            elif request == 'no':
                self.shares = False
                break #Cierra el bucle
            else:
                print("Por favor, responda 'si' o 'no'")  # Pide ingresar el dato de la forma solicitada, en caso de que el usuario ingrese un dato incorrecto.

    # Método para solicitar el cambio del estado de creación de la playlist
    def changeCreator(self):
        # Inicio de un bucle while para obtener la confirmación o negación del usuario sobre la creación de la playlist.
        while True:
            request = input('¿Eres el creador de esta playlist? (si/no): ').strip().lower() #Solicita al usuario confirmar o negar la creación de la playlist quitando elementos innecesarios por medio de strip y normalizando el ingreso de dato.
            if request in ['si', 'sí', 'Si', 'Sí']:
                self.creator = True
                break #Cierra el bucle
            elif request == 'no':
                self.creator = False
                break #Cierra el bucle
            else:
                print("Por favor, responda 'si' o 'no'")  # Pide ingresar el dato de la forma solicitada, en caso de que el usuario ingrese un dato incorrecto.