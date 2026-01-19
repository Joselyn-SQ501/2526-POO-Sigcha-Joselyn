#Trae la opción de recuperar la fecha
from datetime import date

#Importa los modelos existentes en el programa
from models.Cats import DetailsCats
from models.CatHotelDetails import CatHotelDetails

#Subclase de servicios que gestiona la lógica del sistema.
class CatsServices:
    #Creación de un constructor vacío
    def __init__(self):
        self.hotel = CatHotelDetails()  #Inicializa la clase detalles de hotel para gatos

    # Servicios del Hotel
    #Método para configurar la información inicial del hotel
    def setup_hotel(self, name, address, phone, rooms):
        self.hotel.set_hotel_info(name, address, phone)
        self.hotel.set_rooms(rooms)
        self.hotel.set_rooms_status(True)

        # Servicios por defecto
        default_services = [
            "Alimentación premium",
            "Cuidado veterinario básico",
            "Espacio de juegos"
        ]
        #Bucle for para agregar los servicios por defecto configurados internamente.
        for service in default_services:
            self.hotel.add_service(service)
        #Retorna la información del hotel configurado
        return f"Hotel '{name}' configurado exitosamente con {rooms} habitaciones."

    #Método para agregar más servicios al hotel
    def add_hotel_service(self, service):
        self.hotel.add_service(service)
        return f"Servicio '{service}' agregado al hotel."

    #Método para mostrar la información del hotal
    def show_hotel_info(self):
        # Muestra información completa del hotel
        rooms_status = "Disponibles" if self.hotel.get_rooms_status() else "Ocupadas"

        info = f"""
        {'=' * 50}
        HOTEL: {self.hotel.get_name()}
        {'=' * 50}
        Dirección: {self.hotel.get_address()}
        Teléfono: {self.hotel.get_phone()}
        Habitaciones: {self.hotel.get_rooms()} ({rooms_status})
        Gatos alojados: {len(self.hotel.get_cats())}

        Servicios disponibles:
        """
        #Bucle for para imprimir los servicios existentes con numeración
        for i, service in enumerate(self.hotel.get_services(), 1):
            info += f"{i}. {service}\n"

        info += f"{'=' * 50}"
        return info

    # Método que registra un nuevo gato en el sistema
    def register_cat(self, name, color, age):
        cat = DetailsCats()
        cat.set_basic_info(name, color, age)
        self.hotel.add_cat(cat)
        return cat
    # Método setter que establece el estado de salud de un gato
    def set_cat_health_status(self, cat_name, health_status):
        cat = self.hotel.find_cat_by_name(cat_name)
        #Condicional para verificar y actualizar el estado de salud del gato
        if cat:
            cat.set_health_status(health_status)
            return f"Estado de salud de '{cat_name}' actualizado a '{health_status}'😺"
        return f"No se encontró el gato '{cat_name}'🙀"

    #Método para gestionar la adopción del gato
    def manage_cat_adoption(self, cat_name):
        cat = self.hotel.find_cat_by_name(cat_name)
        if not cat:
            return f"No se encontró el gato '{cat_name}'🙀"

        #Bucle while para saber si el gato fue adoptado o no
        while True:
            response = input(f"¿El gato '{cat_name}' ha sido adoptado? (sí/no): ").strip().lower()
            if response == 'sí':
                cat.set_adoption_status(True, date.today())
                return f"¡Felicidades! '{cat_name}' ha sido adoptado😺."
            elif response == 'no':
                cat.set_adoption_status(False)
                return f"'{cat_name}' sigue disponible para adopción😻."
            else:
                print("Respuesta no válida. Por favor, responda 'sí' o 'no'.")

    # Método para establecer la descripción del gato y registra el cambio
    def set_cat_description(self, cat_name, description):
        cat = self.hotel.find_cat_by_name(cat_name)
        #Condicional para crear una descripción y añade el cambio como un registro para el historial médico
        if cat:
            cat.set_description(description)
            cat.add_medical_record({
                'date': date.today(),
                'type': 'descripción',
                'content': description
            })
            return f"Descripción de '{cat_name}' actualizada."
        return f"No se encontró el gato '{cat_name}'"

    #Método para mostrar la información detallada de un gato.
    def show_cat_info(self, cat_name):
        #Solicita el nombre de un gato registrado
        cat = self.hotel.find_cat_by_name(cat_name)
        #Condicional para verificar que el nombre ingresado consta en el sistema, caso contrario muestra que no existe o no se encuentra
        if not cat:
            return f"No se encontró el gato '{cat_name}'"

        adoption_status = "Adoptado" if cat.get_adoption_status() else "Disponible"

        info = f"""
        {'=' * 40}
        GATO: {cat.get_name()}
        {'=' * 40}
        Color: {cat.get_color()}
        Edad: {cat.get_age()} meses
        Fecha de ingreso: {cat.get_enter_date()}
        Estado de salud: {cat.get_health_status()}
        Estado: {adoption_status}
        Descripción: {cat.get_description()}

        Historial médico ({len(cat.get_medical_history())} registros):
        """
        #Bucle for para mostrar los cambios del historial médico enumarado
        for i, record in enumerate(cat.get_medical_history(), 1):
            info += f"  {i}. [{record.get('date', 'N/D')}] {record.get('type', 'registro')}: {record.get('content', record.get('status', 'N/D'))}\n"

        info += f"{'=' * 40}"
        return info

    #Método para retornar la lista de todos los gatos registrados en el hotel
    def list_all_cats(self):
        cats = self.hotel.get_cats()
        if not cats:
            return "No hay gatos registrados en el hotel."

        info = f"\n{'=' * 50}\n"
        info += f"GATOS REGISTRADOS ({len(cats)})\n"
        info += f"{'=' * 50}\n"
        #Bucle for para listar los datos de los gatos registrados
        for i, cat in enumerate(cats, 1):
            status = "✓" if cat.get_adoption_status() else "○"
            info += f"{i:2}. {status} {cat.get_name():15} | {cat.get_color():10} | {cat.get_age():2} meses | Salud: {cat.get_health_status():10}\n"

        info += f"{'=' * 50}"
        return info

    #Método para buscar el estado de adopción de un gato
    def find_cats_by_status(self, adopted=None):
        cats = self.hotel.get_cats()
        if adopted is None:
            return cats
        #Filtra los gatos según su estado de adopción
        filtered = []
        for cat in cats:
            if cat.get_adoption_status() == adopted:
                filtered.append(cat)
        return filtered