#Trae la opción de recuperar la fecha
from datetime import date

# Subclase padre o base para obtener datos del ingreso del gato.
class Cats:
    def __init__(self):
        self.__name_cats = ''# Encapsulación, atributo privado para ingresar el nombre del gato por el usuario como tipo de dato string.
        self.__enter_date_cats = ''# Encapsulación, atributo privado que toma la fecha en que se registra el gato.
    #Método qetter para acceder a la información del gato ingresado
    def get_Information_Cats(self):
        return f"Nombre: {self.__name_cats}, Fecha de ingreso: {self.__enter_date_cats}"

    #Método que aplica polimorfismo de sobreescritura al invocar get_Information_Cats() que puede ser sobreescrito en la clase hija.
    def show_name(self):
        return self.get_Information_Cats()

#Subclase hija o derivada que recopila los detalles de la información del gato (Herencia de la clase Cats)
class DetailsCats(Cats):
    # Creación de un constructor vacío
    def __init__(self):
        super().__init__() #Llamada al constructor de la clase padre.
        self.__color_cats = '' # Encapsulación, atributo privado para ingresar el color del gato por el usuario como tipo de dato string.
        self.__age_cats = 0  # Encapsulación, atributo privado para ingresar la edad del gato por el usuario como tipo de dato integer.
        self.__health_status_cats = '' # Encapsulación, atributo privado para ingresar el estado de salud del gato por el usuario como tipo de dato string.
        self.__adoption_status_cats = False # Encapsulación, atributo privado para preguntar sobre el estado de adopción del gato al usuario como tipo de dato booleano.
        self.description_cats = '' #Atributo público para obtener la descripción del gato por parte del usuario.
        self.__medical_history_cats = [] # Encapsulación, atributo privado sobre el historial médico del gato como un array
        self.__adoption_date_cats = '' # Encapsulación, atributo privado que toma la fecha en que se registra una adopción del gato.
    
    # Método setter básico para establecer la información del gato
    def set_basic_info(self, name, color, age):
        self._Cats__name_cats = name
        self.__color_cats = color
        self.__age_cats = age
        self._Cats__enter_date_cats = date.today()

    # Método setter para establecer el estado de salud del gato
    def set_health_status(self, health_status):
        state_valid = ['excelente', 'bueno', 'regular', 'crítico'] #Array de respuestas esperadas en el sistema sobre el estado de salud del gato
        #Condicional para validar las respuestas ingresadas
        if health_status in state_valid:
            self.__health_status_cats = health_status
            self.__medical_history_cats.append({
                'date': date.today(), #Agrega una fecha al historial clínico
                'status': health_status  #Agrega un estado tras la validación a la historia clínica
            })
        # Si la respuesta no es válida respecto al array devuelve que el estado no es válido
        else:
            raise ValueError("Estado de salud no válido")

    # Método setter para establecer el estado de adopción del gato
    def set_adoption_status(self, status, adoption_date=None):
        self.__adoption_status_cats = status
       # Condicional para verificar si se adopto o no al minino.
        if status and adoption_date:
            self.__adoption_date_cats = adoption_date

    # Método setter para establecer la descripción del gato
    def set_description(self, description):
        self.description_cats = description
    # Método para agregar el historial médico del gato
    def add_medical_record(self, record):
        self.__medical_history_cats.append(record)

    # Métodos Getters para acceder y traer información

    def get_name(self):
        return self._Cats__name_cats

    def get_color(self):
        return self.__color_cats

    def get_age(self):
        return self.__age_cats

    def get_health_status(self):
        return self.__health_status_cats

    def get_adoption_status(self):
        return self.__adoption_status_cats

    def get_enter_date(self):
        return self._Cats__enter_date_cats

    def get_medical_history(self):
        return self.__medical_history_cats

    def get_description(self):
        return self.description_cats

    #POLIMORFISMO DE SOBREESCRITURA
    # Método que extrae y combina la información de la clase padre y de la clase hija
    def show_Information_DetailCats(self):
        info_base = super().get_Information_Cats() #Trae el método de la clase padre y lo reutiliza.
        return f"{info_base}, Color: {self.__color_cats}, Edad: {self.__age_cats} meses"