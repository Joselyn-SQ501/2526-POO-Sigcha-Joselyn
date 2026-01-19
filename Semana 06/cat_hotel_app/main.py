"""
Programa en Python que gestiona un hotel para gatos utilizando Programación
Orientada a Objetos (POO). El sistema aplica herencia, encapsulación y
polimorfismo, organizando el código en clases de modelos, servicios y un
archivo principal con un menú interactivo en consola para administrar la
información del hotel y de los gatos registrados.
"""

#Importa los servicios existentes en el programa
from services.Cats_Services import CatsServices
#Importa los modelos del programa
from  models.Cats import  Cats, DetailsCats

#Método para crear un menú de selección de los procesos existentes en el programa
def display_menu():
    """Muestra el menú principal"""
    print("\n" + "=" * 60)
    print("😻 SISTEMA DE GESTIÓN - HOTEL PARA GATOS 🏩")
    print("=" * 60)
    print("1. Configurar información del hotel ⚙️")
    print("2. Registrar nuevo gato 😺")
    print("3. Gestionar adopción de gato 🐈")
    print("4. Actualizar estado de salud de gato 😺")
    print("5. Agregar descripción a gato 😼")
    print("6. Ver información del hotel 🏨")
    print("7. Ver información de un gato 😸")
    print("8. Listar todos los gatos 🐈🐈‍⬛")
    print("9. Agregar servicio al hotel 🏩")
    print("0. Salir")
    print("=" * 60)

# Clase principal del programa.
class main():
    #Instancia de los servicios
    service = CatsServices()

    # Configuración inicial automática
    print("😻¡Bienvenido al Sistema de Gestión de Hotel para Gatos!🏩")
    print("Configuración inicial del hotel...⚙️")

    #Solicitar al usuario los datos correspondientes al hotel
    hotel_name = input("Nombre del hotel: ").strip()
    address = input("Dirección: ").strip()
    phone = int(input("Teléfono: ").strip())
    rooms = int(input("Número de habitaciones: ").strip())

    #Imprime los datos ingresados
    print(service.setup_hotel(hotel_name, address, phone, rooms))

    #Instancia de la clase del gato padre e hijo
    gato_simple = Cats()
    gato_detallado = DetailsCats()

    # Datos de un gato por defecto para mostrar cómo se comporta un objeto de la clase hija y aplicar polimorfismo al usar métodos heredados y propios después de registrar gatos
    gato_detallado.set_basic_info("Mishu", "negro", 24)
    print("El gatito actualmente hospedado es:")
    print(f"  Nombre: {gato_detallado.get_name()}")
    print(f"  Color: {gato_detallado.get_color()}")
    print(f"  Age: {gato_detallado.get_age()} meses")

    #Bucle while para evaluar por medio de un condicional la selección del menú inicial
    while True:
        display_menu()
        choice = input("\nSeleccione una opción (0-9): ").strip()

        # Sí la opción seleccionada es 0 se finaliza el programa
        if choice == "0":
            print("¡Gracias por usar este sistema gatuno!😺¡Buen día!✨")
            break

        # Sí la opción seleccionada es 1 se reconfigura la información ingresada del hotel gatuno
        elif choice == "1":
            print("\n--- CONFIGURAR HOTEL 🏨---")
            name = input("Nuevo nombre del hotel: ").strip()
            address = input("Nueva dirección: ").strip()
            phone = int(input("Nuevo teléfono: ").strip())
            rooms = int(input("Nuevo número de habitaciones: ").strip())

            print(service.setup_hotel(name, address, phone, rooms))

        # Sí la opción seleccionada es 2 se registra información de un gato nuevo
        elif choice == "2":
            print("\n--- REGISTRAR NUEVO GATO 😸 ---")
            name = input("Nombre del gato: ").strip()
            color = input("Color: ").strip()
            age = int(input("Edad (en meses): ").strip())

            cat = service.register_cat(name, color, age)

            # Pregunta por el estado de salud del gato
            set_health = input("¿Establecer estado de salud ahora? (sí/no): ").strip().lower()
            if set_health == 'sí':
                health = input("Estado (excelente/bueno/regular/crítico): ").strip().lower()
                print(service.set_cat_health_status(name, health))

            print(f"Gato '{name}' registrado exitosamente.")

        # Sí la opción seleccionada es 3 se abre el proceso sobre adopción de un minino ingresado
        elif choice == "3":
            print("\n--- GESTIONAR ADOPCIÓN ---")
            name = input("Nombre del gato: ").strip()
            print(service.manage_cat_adoption(name))

        # Sí la opción seleccionada es 4 se actualiza el estado de salud del minino
        elif choice == "4":
            print("\n--- ACTUALIZAR ESTADO DE SALUD ---")
            name = input("Nombre del gato: ").strip()
            health = input("Nuevo estado (excelente/bueno/regular/crítico): ").strip().lower()
            print(service.set_cat_health_status(name, health))

        # Sí la opción seleccionada es 5 se agrega una descripción del minino
        elif choice == "5":
            print("\n--- AGREGAR DESCRIPCIÓN ---")
            name = input("Nombre del gato: ").strip()
            description = input("Descripción: ").strip()
            print(service.set_cat_description(name, description))

        # Sí la opción seleccionada es 6 se muestra la información que se tiene del hotel
        elif choice == "6":
            print("\n--- INFORMACIÓN DEL HOTEL 🏨---")
            print(service.show_hotel_info())

        # Sí la opción seleccionada es 7 se muestra la información que se tiene del gato
        elif choice == "7":
            print("\n--- INFORMACIÓN DE GATO 😸 ---")
            name = input("Nombre del gato: ").strip()
            print(service.show_cat_info(name))

        # Sí la opción seleccionada es 8 se muestra la lista de todos los gatos registrados
        elif choice == "8":
            print("\n--- LISTA DE GATOS 🐈‍⬛🐈---")
            print(service.list_all_cats())

        # Sí la opción seleccionada es 9 permite agregar un servicio nuevo al sistema
        elif choice == "9":
            print("\n--- AGREGAR SERVICIO ---")
            new_service = input("Nuevo servicio a agregar: ").strip()
            print(service.add_hotel_service(new_service))

        #Solicita ingresar una opción válida del menú
        else:
            print("Opción no válida. Por favor, seleccione una opción del 0 al 9.")

        #Permite continuar con otro proceso del menú
        input("\nPresione Enter para continuar...")