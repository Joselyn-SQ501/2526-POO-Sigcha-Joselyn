#Impora os módulos necesarios
import os

# Creación de una clase de servicio para manejar archivos
class FileService:
    
    # Se define un método estático dentro de la clase que no requiere una instancia de la clase para ser utilizado
    @staticmethod
    
    # Udo del método para mostrar el código de un script, mismo que fue obtenido del archivo original Dashboard.py
    def mostrar_codigo(ruta_script):
        ruta_script_absoluta = os.path.abspath(ruta_script)
        try:
            with open(ruta_script_absoluta, 'r') as archivo:
                codigo = archivo.read()
                print(f"\n--- Código de {ruta_script} ---\n")
                print(codigo)
                return codigo
        except FileNotFoundError:
            print("El archivo no se encontró.")
        except Exception as e:
            print(f"Ocurrió un error al leer el archivo: {e}")
        return None
