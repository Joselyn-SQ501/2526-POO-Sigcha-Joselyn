"""
Programa en Python que analiza información básica de playlists utilizando
distintos tipos de datos (int, float, str, bool) y identificadores descriptivos
en snake_case, con el fin de determinar un perfil de usuario y generar
recomendaciones generales de uso según hábitos de consumo.
"""

#Importa los servicios existentes en el programa
from servicios.PlaylistService import calculate_total_duration, analyze_playlist, get_recommendation, show_result, \
    type_user_idetification
#Importa las clases existentes en el programa
from modelos.PlaylistDetails import PlaylistDetails
from modelos.User import User
from modelos.ListeningHabits import ListeningHabits

# Clase principal del programa.
class main:
    print("="*50)
    print("=== 🎵 ANALIZADOR DE PLAYLISTS 🎵  ===")
    print("="*50)
    
    playlists_analyzed = 0 # Contador para determinar las veces en las que se analiza diferentes playlists.

    # Inicio del bucle while para realizar el análisis de las playlists varias veces.
    while True:
            # Crea instancias de las clases
            playlist = PlaylistDetails()
            user = User()
            habits = ListeningHabits()
            
            # Solicitar datos usando los métodos del servicio
            print("\n=== INGRESO DE DATOS DE LA PLAYLIST ===\n")
            playlist.enter_details()  # Llama al método para ingresar los datos de la playlist.
            print("\n--- HÁBITOS DE ESCUCHA ---")
            habits.enter_playlist() # Llama al método para ingresar los hábitos de escucha de la playlist,

            # Muestra el resumen de la información ingresada por el usuario.
            print(f'\n=== RESUMEN DE LA PLAYLIST ===')
            print(f'Tu playlist es: {playlist.name}')
            print(f'La cantidad de canciones que tiene son: {playlist.total_songs} canciones')
            print(f'La duración promedio por canción es: {playlist.average_duration_music} minutos')
            print(f'El formato es: {playlist.media_format}')
            print(f'El número de veces que has escuchado la playlist es: {habits.plays} veces')
            print(f'En cuánto a las interacciones {"Sí" if habits.likes else "No"} diste me gusta,')
            print(f'{"Sí" if habits.comments else "No"} comentaste y {"Sí" if habits.shares else "No"} compartiste.')
            print(f'Además, {"Si" if habits.creator else "No"} eres creador')
            print(f"\nGracias a todo estos datos, se determina que:")

            # Realiza los análisis usando métodos del servicio
            total_duration = calculate_total_duration(playlist) # Utiliza el método para calcular la duración total.
            is_long_playlist = analyze_playlist(total_duration) # Manda la duración total para ser analizada en el método correspondiente.
            recommendation = get_recommendation(is_long_playlist) # Trae la recomendación de acuerdo con el análisis realizado.
            type_user_idetification(user, habits) # Retorna el tipo de usuario identificado en base al análisis
            # Muestra los análisis realizados
            show_result(playlist, total_duration, recommendation, habits, user)

            playlists_analyzed += 1 # Aumenta el contador de las playlists analizadas,
            
            continuar = input("\n¿Desea analizar otra playlist? (si/no): ").strip().lower() # Atributo para definir si se desea analizar otra playlist o terminar el proceso.
            if continuar not in ['si', 'sí', 'Si', 'Sí']:  # Condicional para continuar los análisis mientras no se ingrese no.
                print(f"\n{'='*50}")
                print(f"Playlists analizadas: {playlists_analyzed}")
                print("\n¡Gracias por usar el analizador de Playlist!😺🎵¡Buen día!✨")
                print(f"{'='*50}")
                break
            print("\n" + "="*50 + "\n")

