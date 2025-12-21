# Subclase para ingresar los atributos del gato
class datos_gatos:
    # Creación de un constructor vacío
    def __init__(self):
        self.nombre = ""  # Atributo del nombre del gato o gata ingresado por el usuario
        self.edad = 0  # Atributo de la edad del gato o gata ingresado por el usuario
        self.peso = 0.0 # Atributo del peso del gato o gata ingresado por el usuario
        self.color = "" # Atributo del color del gato o gata ingresado por el usuario
        self.cuidador = "" # Atributo del nombre del cuidador del gato o gata ingresado por el usuario
        self.validar = False #Atributo de validación de información

    # Método para solicitar los datos del gato al usuario
    def datos_pedidos(self):
        self.nombre = input("Ingrese el nombre del gato o gata: ")
        self.edad = int(input("Ingrese la edad del gato o gata (en meses): "))
        self.peso = float(input("Ingrese el peso del gato o gata (en kg): "))
        self.color = input("Ingrese el color del gato o gata: ")
        self.cuidador = input("Ingrese el nombre del cuidador del gato o gata: ")

    # Método para mostrar los datos ingresados y validar los datos
    def mostrar_datos(self):
        print("\nDatos del Michi ingresados por favor validar:")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} meses")
        print(f"Peso: {self.peso} kg")
        print(f"Color: {self.color}")
        print(f"Cuidador: {self.cuidador}")

        # Imprime la condición con la que se van a validar los datos
        print("\n¿Son correctos los datos ingresados?")
        print("1. Sí")
        print("2. No")

        opcion = input("Seleccione una opción (1 o 2): ")

        # Validación de los datos ingresados por medio de una condición numérica
        if opcion == "1":
            self.validar = True
        else:
            self.validar = False

    # Método que verifica si los datos fueron validados
    def validar_datos(self):
        if self.validar == True:
            print("\n¡Los datos han sido validados correctamente!")
        # Si no son correctos, vuelve a solicitar los datos
        else:
            print("\nPor favor, ingrese nuevamente los datos del gato o gata.")
            datos_gatos.datos_pedidos(self)