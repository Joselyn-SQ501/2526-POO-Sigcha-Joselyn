# Subclase para ingresar datos sobre el entretenimiento del gato
class entretenimiento_gatos:
    # Creación de un constructor vacío
    def __init__(self):
        self.juguetes = [] # Atributo de los juguetes que usa el gato o gata para su entretenimiento ingresados por el usuario
        self.horas_juego_diarias = 0 # Atributo de las horas de juego diarias del gato o gata ingresadas por el usuario
        self.actividades_favoritas = [] # Atributo de las actividades favoritas del gato o gata ingresadas por el usuario
        self.validar_entretenimiento = False # Atributo de validación de información

    # Método para solicitar los datos sobre el entretenimiento o juego del gato o gata al usuario
    def seleccionar_entretenimiento(self):
        print("\nIngrese los juguetes con los que el gato o gata juegan (ingrese 'fin' para terminar): ")
        # Bucle para solicitar el ingreso de juguetes que usa el gato o gata que irán agregándose al atributo juguetes
        while True:
            juguete = input("Ingrese el nombre del juguete: ")
            if juguete.lower() == 'fin': # Condición que permite terminar el bucle de la información solicitada
                break
            self.juguetes.append(juguete)

        self.horas_juego_diarias = int(input("Ingrese las horas diarias de juego: "))

        print("\nIngrese las actividades favoritas del gato o gata (ingrese 'fin' para terminar): ")
        # Bucle para solicitar el ingreso de varias actividades favoritas del gato que irán agregándose al atributo actividades favoritas
        while True:
            actividad = input("Ingrese la actividad favorita: ")
            if actividad.lower() == 'fin': # Condición que permite terminar el bucle de la información solicitada
                break
            self.actividades_favoritas.append(actividad)

    # Método para mostrar los datos ingresados y validar los datos
    def mostrar_entretenimiento(self):
        print("\nResumen del entretenimiento seleccionado: ")
        print("Juguetes seleccionados: ")
        # Lee el array del atributo juguetes
        for juguete in self.juguetes:
            print(f"- {juguete}")
        print(f"Horas diarias de juego: {self.horas_juego_diarias}")
        print("Actividades favoritas: ")
        # Lee el array del atributo actividades favoritas
        for actividad in self.actividades_favoritas:
            print(f"- {actividad}")

    # Método que imprime la condición con la que se van a validar los datos
    def validar_entretenimiento_seleccionado(self):
        print("\n¿Son correctos los datos sobre el entretenimiento de su michi?")
        print("1. Sí")
        print("2. No")

        opcion = input("Seleccione una opción (1 o 2): ")

        # Validación de los datos ingresados por medio de una condición numérica
        if opcion == "1":
            self.validar_entretenimiento = True
            print("\n¡El entretenimiento ha sido validado correctamente 😺!")
        else:
            self.validar_entretenimiento = False
            print("\nPor favor, ingrese nuevamente el entretenimiento del gato o gata 🙀")
            entretenimiento_gatos.seleccionar_entretenimiento(self)