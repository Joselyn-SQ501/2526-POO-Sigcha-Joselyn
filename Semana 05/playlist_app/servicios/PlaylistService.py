# Método para calcular la duración total de la playlist
def calculate_total_duration(playlist):
    # Retorna el cálculo la duración total de la playlist.
    return playlist.total_songs * playlist.average_duration_music

# Método para analizar la duración de la playlist.
def analyze_playlist(total_duration):
    """
    Analiza si la playlist es corta o larga.
    Retorna un boolean (True si es larga).
    """
    return total_duration >= 60

# Método para hacer una recomendación de uso general de la playlist dependiendo de su duración total.
def get_recommendation(is_long_playlist):
    # Devuelve una recomendación según la duración.
    if is_long_playlist:
        return "recomienda para acompañar actividades prolongadas, proporcionando continuidad y ambientación durante distintos momentos del día."
    else:
        return "recomienda para usos puntuales o sesiones breves, ideales para mantener la atención y organizar mejor el tiempo de escucha."

# Método para mostrar el análisis final de los datos obtenidos sobre la playlist.
def show_result(playlist, total_duration, recommendation, habits, user):
    """Muestra el análisis final."""
    print("\n=== ANÁLISIS DE LA PLAYLIST ===")
    print(f"Tu playlist se llama: {playlist.name}")
    print(f"Tiene una duración total de: {total_duration:.2f} minutos") # Muestra la duración total de la playlist con máximo dos decimales.
    print(f"Por lo que se considera una playlist {'Larga' if total_duration >= 60 else 'Corta'}")
    # Muestra la recomendación según la duración
    print(f"Por esta razón, esta playlist se {recommendation}")

    # Análisis del formato ingresado por medio de una condicional para generar recomendaciones sobre el uso de la playlist en diferentes actividades.
    if playlist.media_format.lower() == 'mp3':
        print("- 🎵 Adicionalmente por el formato MP3 es una playlist adecuada para cuando estas estudiando, en el trabajo o realizando una actividad practica, ya que permite concentrarse en el audio sin distracciones visuales.")
    elif playlist.media_format.lower() == 'mp4':
        print("- 🎬 Adicionalmente por el formato MP4 es una playlist adecuada para contenidos en los que requieras apoyo visual, donde la imagen complementa y mejora la comprensión de tu contenido.")
    
    # Análisis de los hábitos de escucha de la playlist catalogándolos en base a los datos registrados por el usuario por medio de condicionales.
    # Condicional para determinar que tan frecuentemente interactúa el usuario con la playlist.
    if habits.plays > 50:
        print("- ⭐ También has interactuado frecuentemente con esta playlist")
    elif habits.plays > 25:
        print("- 👍 También has interactuado regularmente con esta playlist")
    else:
        print("- 🔍 También has interactuado ocasionalmente con esta playlist")

    # Condicional para determinar si al usuario le gustó la playlist.
    if habits.likes:
        print("- ❤️ Además, te ha gustado.")
    else:
        print("- ️💔 Además no te ha gustado.")

    # Condicional para determinar si el usuario comentó la playlist.
    if habits.comments:
            print("- 💬 Has comentado.")
    else:
        print("- 💬 No has comentado.")

    # Condicional para determinar si el usuario compartió la playlist.
    if habits.shares:
            print("- 🔗 Y has compartido con otros.")
    else:
        print("- 🔗 Y no has compartido con otros.")

    # Imprime el mensaje sobre el tipo de usuario que es en base al análisis.
    print(f'Finalmente, el último punto a analizar en base a tus respuestas sobre tu playlist {playlist.name} es que eres un usuario: {user.user_type}')

# Método para analizar el tipo de usuario de la playlist.
def type_user_idetification(user, habits):
    type = ''
    if habits.plays > 25:  # Condicional para definir si el tipo de usuario es consumidor
       type += 'Consumidor'

    if habits.likes or habits.comments or habits.shares: # Condicional para definir si el tipo de usuario es participativo siempre y cuando cumpla con un aspecto de la condición
        type += " Participativo"

    if habits.creator: # Condicional para definir si el tipo de usuario es creador
        type += " Creador"

    user.user_type = type # El valor de la variable type es ingresada en el atributo user_type de la clase user.