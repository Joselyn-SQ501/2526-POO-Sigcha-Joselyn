# Subclase para ingresar la dieta del gato
class dieta_gatos:
    # Creación de un constructor vacío
    def __init__(self):
        self.tipo_dieta = "" # Atributo del tipo de dieta del gato o gata ingresado por el usuario
        self.croquetas_diarias = 0 # Atributo de la cantidad de croquetas ingeridas por el gato o gata ingresado por el usuario
        self.comida_carnes = 0.0 # Atributo de la cantidad de carnes ingeridas por gato o gata ingresado por el usuario
        self.hidratacion = "" # Atributo del medio de hidratación del gato o gata ingresado por el usuario
        self.validar_dieta = False #Atributo de validación de información

    # Método para solicitar los datos de la dieta del gato al usuario
    def dieta_dia(self):
        print("\nSeleccione el tipo de dieta para el gato o gata:")
        print("1. Dieta de croquetas")
        print("2. Dieta de comida casera (carnes)")
        print("3. Dieta mixta (croquetas y comida casera)")

        opcion = input("Ingrese el número correspondiente a la dieta elegida (1, 2 o 3) : ")

        # Condicional para la elección del tipo de dieta del gato o gata
        if opcion == "1": # Solicita los datos del tipo de dieta croquetas más hidratación
            self.tipo_dieta = "Dieta de croquetas"
            self.croquetas_diarias = int(input("Ingrese la cantidad diaria de croquetas (en gramos): "))
            self.hidratacion = input('Su gatito tiene agua o leche para acompañar las croquetas? (Ingrese "agua" o "leche" o "ninguno"): ')
        # Solicita los datos del tipo de dieta casera más hidratación
        elif opcion == "2":
            self.tipo_dieta = "Dieta de comida casera"
            self.comida_carnes = float(input("Ingrese la cantidad diaria de comida casera (en kg): "))
            self.hidratacion = input(
                'Su gatito tiene agua o leche para acompañar las croquetas? (Ingrese "agua" o "leche" o "ninguno"): ')
        # Solicita los datos del tipo de dieta croquetas y casera  más hidratación
        elif opcion == "3":
            self.tipo_dieta = "Dieta mixta"
            self.croquetas_diarias = int(input("Ingrese la cantidad diaria de croquetas (en gramos): "))
            self.comida_carnes = float(input("Ingrese la cantidad diaria de comida casera (en kg): "))
            self.hidratacion = input(
                'Su gatito tiene agua o leche para acompañar las croquetas? (Ingrese "agua" o "leche" o "ninguno"): ')
        # Solicita el ingreso de un dato válido según las opciones mostradas
        else:
            print("Opción no válida. Por favor, intente nuevamente.")
            dieta_gatos.dieta_dia(self)

    # Método para mostrar los datos ingresados y validar los datos
    def mostrar_dieta(self):
        print("\nResumen de la dieta seleccionada:")
        print(f"Tipo de dieta: {self.tipo_dieta}")
        if self.tipo_dieta == "Dieta de croquetas":
            print(f"Cantidad diaria de croquetas: {self.croquetas_diarias} gramos")
        elif self.tipo_dieta == "Dieta de comida casera":
            print(f"Cantidad diaria de comida casera: {self.comida_carnes} kg")
        elif self.tipo_dieta == "Dieta mixta":
            print(f"Cantidad diaria de croquetas: {self.croquetas_diarias} gramos")
            print(f"Cantidad diaria de comida casera: {self.comida_carnes} kg")

    # Imprime la condición con la que se van a validar los datos
    def validar_dieta_seleccionada(self):
        print("\n¿Es correcta la dieta seleccionada?")
        print("1. Sí")
        print("2. No")

        opcion = input("Seleccione una opción (1 o 2): ")

        # Validación de los datos ingresados por medio de una condición numérica
        if opcion == "1":
            self.validar_dieta = True
            print("\n¡La dieta ha sido validada correctamente!")
        else:
            self.validar_dieta = False
            print("\nPor favor, seleccione nuevamente la dieta del gato o gata.")
            dieta_gatos.dieta_dia(self)

    # Método que valida la hidratación felina
    def validar_suplemento_liquido(self):
        if self.hidratacion == "agua":
            print("\nEl gato o gata tiene agua para acompañar su dieta.")
        elif self.hidratacion == "leche":
            print("\nEl gato o gata tiene leche para acompañar su dieta.")
        else:
            print(
                "\nEl gato o gata no tiene ningún medio de hidratación para acompañar su dieta, recuerde siempre incorporar agua o leche según sea necesario para su hidratación.")