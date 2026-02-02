# Importa la fecha y hora actuales
from datetime import datetime
# Importa el módulo os para manejar rutas de archivos
import os

# Creación de una clase de servicio para manejar el historial de ejecuciones
class HistoryService:
    # Define el nombre del archivo donde se guardará el historial
    HISTORIAL_FILE = "historial.txt"
    # Creación de un método estático para guardar la información de ejecución de un script 
    @staticmethod
    def guardar(ruta_script):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Establece un formato de fecha y hora actuales
        linea = f"{fecha} - Ejecutado: {ruta_script}\n" # Establece la línea a guardar en el historial
        
        # Intenta abrir el archivo de historial en modo de anexado y escribir la línea
        try:
            with open(HistoryService.HISTORIAL_FILE, "a", encoding="utf-8") as f:
                f.write(linea)
        # Captura cualquier excepción que ocurra durante la escritura del archivo
        except Exception as e:
            print(f"Error al guardar historial: {e}")
