#Descripción:
# Este programa en Python recoge datos de las temperaturas diarias de una semana y calcula los promedios
# de temperatura semanal bajo un enfoque de Programación Orientada a Objetos (POO).

#Importa las clases de ingreso de temperatura y cálculo de la temperatura semanal.
from ingreso_temperature import ingreso_temperatura
from calculo_temperature import calculo_temperatura

#Clase principal del programa.
class main:
    print("\nPrograma de registro y cálculo de temperatura semanal")
    print("\nTemperaturas de los 7 días de la semana")
    # Instancia de la clase del ingreso de la temperatura.
    ingreso = ingreso_temperatura()
    # Utiliza la instancia creada llamada ingreso para llamar al método ingresar temperatura.
    temperaturas = ingreso.ingresar_temperatura()

    print("\nPromedio de las temperaturas registradas")
    # Instancia de la clase del cálculo de temperatura.
    calculo = calculo_temperatura()
    # La instancia de cálculo obtiene el atributo de temperatura para guardar los datos ingresados en
    # la clase de ingreso de temperatura por medio de su instancia llamada ingreso.
    calculo.temperatura = ingreso.temperatura
    # Utiliza la instancia creada llamada calculo para ejecutar el método de la suma de temperatura.
    calculo.suma_temperaturas()
    # Utiliza la instancia creada llamada calculo para llamar al método del promedio de temperatura.
    calculo.promedio_temperaturas()
    print("\nCálculo completado.")

print("\n😺¡Buen día!✨")