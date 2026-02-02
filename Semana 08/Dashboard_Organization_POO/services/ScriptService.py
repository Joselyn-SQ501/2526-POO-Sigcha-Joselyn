# Uso de las importaciones del archivo original Dashboard.py
import os
import subprocess # Importa el módulo subprocess para ejecutar nuevos procesos
from services.HistoryService import HistoryService # Importa la clase de servicio de historial

# Creación de una clase de servicio para manejar la ejecución de scripts
class ScriptService:
    # Definición de un método estático para ejecutar el código de un script
    @staticmethod
    # Uso del método para ejecutar el código de un script, mismo que fue obtenido del archivo original Dashboard.py
    def ejecutar_codigo(ruta_script):
        try:
            HistoryService.guardar(ruta_script) # Creación de un historial de scripts ejecutados
            if os.name == 'nt':  # Windows
                subprocess.Popen(['cmd', '/k', 'python', ruta_script])
            else:  # Unix-based systems
                subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
        except Exception as e:
            print(f"Ocurrió un error al ejecutar el código: {e}")
