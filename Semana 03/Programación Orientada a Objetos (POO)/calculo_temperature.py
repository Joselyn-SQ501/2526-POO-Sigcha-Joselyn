#Subclase para calcular la temperatura de una semana.
class calculo_temperatura:
    # Creación de un constructor vacío
    def __init__(self):
        self.temperatura = [] # Atributo heredado de la temperatura ingresada en la instancia ingreso.
        self.suma = 0 # Atributo suma inicializado en 0.

    # Método para sumar la temperatura.
    def suma_temperaturas(self):
        #Bucle for para sumar la temperatura.
        for i in range(len(self.temperatura)):
            self.suma += self.temperatura[i]
        #Imprime el resultado de la suma.
        print('La suma de las temperaturas es: ', self.suma)

    # Método para calcular el promedio de la temperatura.
    def promedio_temperaturas(self):
        promedio_temperatura = self.suma / 7  #Cálculo del promedio de la temperatura.
        #imprime el promedio de la temperatura semanal en °C.
        print(f'El promedio de las temperaturas es: {promedio_temperatura:.2f} °C')