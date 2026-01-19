# Subclase para ingresar datos sobre el hotel gatuno.
class CatHotelDetails:

    # Creación de un constructor vacío
    def __init__(self):
        self.__name_hotel = '' # Encapsulación, atributo privado para ingresar el nombre del hotel por el usuario como tipo de dato string.
        self.__address_hotel = '' # Encapsulación, atributo privado para ingresar la dirección por el usuario como tipo de dato string.
        self.__phone_hotel = 0 # Encapsulación, atributo privado para ingresar el teléfono del hotel por el usuario como tipo de dato integer.
        self.__services_hotel = [] # Encapsulación, atributo privado para ingresar los servicios del hotel por el usuario como un array.
        self.__rooms_hotel = 0 # Encapsulación, atributo privado para ingresar el número de habitaciones por el usuario como tipo de dato integer.
        self.__rooms_status = False # Encapsulación, atributo privado para comprobar el estado de las habitaciones del hotel como tipo de dato booleano.
        self.__cats_list = [] # Encapsulación, atributo privado que los gatos del hotel como un array.

    # Método setter básico para establecer la información del hotel gatuno
    def set_hotel_info(self, name, address, phone):
        self.__name_hotel = name
        self.__address_hotel = address
        self.__phone_hotel = phone

    # Método setter para establecer el número de habitaciones del hotel felino
    def set_rooms(self, rooms):
        self.__rooms_hotel = rooms

    # Método setter para establecer el estado de disponibilidad de las habitaciones del hotel gatuno
    def set_rooms_status(self, status):
        self.__rooms_status = status

    # Método setter para añadir un servicio en el hotel
    def add_service(self, service):
        self.__services_hotel.append(service)

    # Método setter básico para determinar una lista de los gatos existentes en el hotel
    def add_cat(self, cat):
        self.__cats_list.append(cat)
    
    # Métodos getter para acceder y mostrar la información del hotel
    def get_name(self):
        return self.__name_hotel
    
    def get_address(self):
        return self.__address_hotel
    
    def get_phone(self):
        return self.__phone_hotel
    
    def get_services(self):
        return self.__services_hotel
    
    def get_rooms(self):
        return self.__rooms_hotel
    
    def get_rooms_status(self):
        return self.__rooms_status
    
    def get_cats(self):
        return self.__cats_list

    # Método getter para buscar el nombre de un gato existente ingresado de la lista
    def find_cat_by_name(self, name):
        for cat in self.__cats_list:
            if cat.get_name() == name:
                return cat
        return None