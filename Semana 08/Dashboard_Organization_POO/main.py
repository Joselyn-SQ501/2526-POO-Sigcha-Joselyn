# Importa los modelos disponibles
from model.MenuModel import MenuModel
# Importa el servicio de menú que junta todos los servicios existentes
from services.MenuService import MenuService

#Creación de la función principal del programa
def main():
    menu_model = MenuModel() # Instancia de la clase MenuModel
    menu_service = MenuService(menu_model) # Instancia del servicio de menú
    menu_service.mostrar_menu()  # Ejecucuón de la función mostrar menú

# Inicializa la función main, obtenido del archivo original Dashboard.py
if __name__ == "__main__":
    main()
