# Subclase para ingresar la rutina del gato
class rutina_gato:
    def __init__(self):
        # Creación de un constructor vacío
        self.horas_actividad_diaria = 0 # Atributo de las horas de actividad diarias del gato o gata ingresadas por el usuario
        self.tipo_actividad = "" # Atributo del tipo de actividad que realiza el gato o gata ingresado por el usuario
        self.lugares_favoritos = [] # Atributo de los espacios favoritos del gato o gata ingresados por el usuario
        self.validar_rutina = False # Atributo de validación de información

    # Método para solicitar los datos sobre la rutina del gato o gata al usuario
    def definir_rutina(self):
        self.horas_actividad_diaria = int(input("Ingrese las horas diarias de actividad del gato o gata: "))
        self.tipo_actividad = input("Ingrese el tipo de actividad favorita del gato o gata (ej. caza, exploración, descanso, paseo): ")

        print("\nIngrese los lugares favoritos del gato o gata (ingrese 'fin' para terminar): ")
        # Bucle para solicitar el ingreso de varios lugares favoritos del gato que irán agregándose al atributo lugares favoritos
        while True:
            lugar = input("Ingrese un lugar favorito: ")
            if lugar.lower() == 'fin': #  Condición que permite terminar el bucle de la información solicitada
                break
            self.lugares_favoritos.append(lugar)

    # Método para mostrar los datos ingresados y validar los datos
    def mostrar_rutina(self):
        print("\nResumen de la rutina definida:")
        print(f"Horas diarias de actividad: {self.horas_actividad_diaria}")
        print(f"Tipo de actividad favorita: {self.tipo_actividad}")
        print("Lugares favoritos:")
        # Lee el array del atributo de lugares favoritos
        for lugar in self.lugares_favoritos:
            print(f"- {lugar}")

    # Método que imprime la condición con la que se van a validar los datos
    def validar_rutina_definida(self):
        print("\n¿Es correcta la rutina definida?")
        print("1. Sí")
        print("2. No")

        opcion = input("Seleccione una opción (1 o 2): ")

        # Validación de los datos ingresados por medio de una condición numérica
        if opcion == "1":
            self.validar_rutina = True
            print("\n¡La rutina ha sido validada correctamente 😺!")
        else:
            self.validar_rutina = False
            print("\nPor favor, defina nuevamente la rutina del gato o gata 🙀.")
            rutina_gato.definir_rutina(self)