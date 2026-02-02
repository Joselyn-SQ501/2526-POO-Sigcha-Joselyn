import os
# Importa los servicios disponibles
from services.FileService import FileService
from services.ScriptService import ScriptService

# Creación de una clase de servicio para manejar el menú principal y submenús
class MenuService:
    # Creación de un constructor
    def __init__(self, menu_model):
        self.menu_model = menu_model  # Atributo para usar las opciones del menú
        self.ruta_base = os.path.dirname(__file__)  # Atributo para usar los archivos del menú
        self.ruta_base = os.path.dirname(self.ruta_base)  # Atributo para buscar o que trae la dirección del archivo

    # Uso de los métodos del archivo original Dashboard.py, ambios en los mensajes de salida, bucles y pequeños aspectos de los condicionales
    def mostrar_menu(self):
        while True:
            print("\nMenu Principal - Dashboard")
            # Imprime las opciones del menú principal
            for key, value in self.menu_model.unidades.items():
                print(f"{key} - {value}")
            print("0 - Salir")

            eleccion_unidad = input("Elige una unidad o '0' para salir: ")

            if eleccion_unidad == '0':
                print("Saliendo del programa.")
                break
            elif eleccion_unidad in self.menu_model.unidades:
                ruta = os.path.join(self.ruta_base, self.menu_model.unidades[eleccion_unidad])
                self.mostrar_sub_menu(ruta)
            else:
                print("Opción no válida.")

    def mostrar_sub_menu(self, ruta_unidad):
        sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

        while True:
            print("\nSubmenú - Selecciona una subcarpeta")
            # Imprime las subcarpetas
            for i, carpeta in enumerate(sub_carpetas, 1):
                print(f"{i} - {carpeta}")
            print("0 - Regresar")

            eleccion_carpeta = input("Elige una opción: ")

            if eleccion_carpeta == '0':
                break
            try:
                index = int(eleccion_carpeta) - 1
                if 0 <= index < len(sub_carpetas):
                    self.mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[index]))
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Opción no válida.")

    def mostrar_scripts(self, ruta_sub_carpeta):
        scripts = [f.name for f in os.scandir(ruta_sub_carpeta)
                   if f.is_file() and f.name.endswith('.py')]

        while True:
            print("\nScripts")
            for i, script in enumerate(scripts, 1):
                print(f"{i} - {script}")
            print("0 - Regresar")
            print("9 - Menú principal")

            eleccion_script = input("Elige un script: ")

            if eleccion_script == '0':
                break
            elif eleccion_script == '9':
                return
            else:
                try:
                    index = int(eleccion_script) - 1
                    if 0 <= index < len(scripts):
                        ruta_script = os.path.join(ruta_sub_carpeta, scripts[index])
                        codigo = FileService.mostrar_codigo(ruta_script)
                        if codigo:
                            ejecutar = input("¿Ejecutar? (1: Sí, 0: No): ")
                            if ejecutar == '1':
                                ScriptService.ejecutar_codigo(ruta_script)
                            elif ejecutar == '0':
                                print("No se ejecutó el script.")
                            else:
                                print("Opción no válida. Regresando al menú de scripts.")
                            input("\nPresiona Enter para continuar...")
                    else:
                        print("Opción no válida.")
                except ValueError:
                    print("Opción no válida.")
