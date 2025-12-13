# Subclase para ingresar la temperatura diaria de una semana del programa.
class ingreso_temperatura:
    # Creación de un constructor vacío
    def __init__(self):
        self.dia = []  # Atributo del día de la semana ingresado por el usuario.
        self.temperatura = []  # Atributo de la temperatura ingresado por el usuario.

    # Método para ingresar la temperatura.
    def ingresar_temperatura(self):
        # Bucle for para ingresar los 7 días de la semana con su respectiva temperatura.
        for i in range(7):
            dia_semana = input('\nIngrese el día de la semana: ')
            temperaturas = int(input('Ingrese la temperatura del día: '))
            # Agrega los datos ingresados a a sus correspondientes atributos.
            self.dia.append(dia_semana) #Agrega al atributo día.
            self.temperatura.append(temperaturas) #Agrega al atributo temperatura.
            # Imprime los datos ingresados.
            print(f'Día {self.dia[i]} ha registrado:', self.temperatura[i], '°C')