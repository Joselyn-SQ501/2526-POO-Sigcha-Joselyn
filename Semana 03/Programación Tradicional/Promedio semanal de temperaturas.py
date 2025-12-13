#Descripción:
# Este programa en Python recoge datos de las temperaturas diarias de una semana y calcula los promedios
# de temperatura semanal bajo un enfoque de programación tradicional.

print("\nCalcular el promedio de temperatura semanal")

#Inicia la función central de la temperatura.
def temperatura():
    dia = [] #Aquí se guarda el día de la semana ingresado por el usuario.
    temperatura = []  #Aquí se guarda los datos de la temperatura que el usuario registre por día.

    #Bucle for para ingresar los 7 días de la semana con su respectiva temperatura.
    for i in range(7):
        dia_semana = input('\nIngrese el día de la semana: ')
        temperaturas = int(input('Ingrese la temperatura del día: '))
        #Agrega los datos ingresados a sus respectivos arrays.
        dia.append(dia_semana) #Agrega a array día.
        temperatura.append(temperaturas) #Agrega a array temperatura.
        #Imprime los datos ingresados.
        print(f'Día {dia[i]} ha registrado:', temperatura[i], '°C')
    #Manda el valor del array temperatura para calcular el promedio de temperatura semanal.
    calcular_promedio(temperatura)

#Función para calcular el promedio de la temperatura semanal.
def calcular_promedio(temperatura):
    #Inicialización de variables para la suma y promedio de temperatura semanal.
    suma_temperatura = 0
    promedio_temperatura = 0

    #Bucle for para sumar las temperaturas ingresadas.
    for j in range(len(temperatura)):
        suma_temperatura += temperatura[j]
    #Calculo del promedio de temperatura semanal.
    promedio_temperatura = suma_temperatura / 7
    #imprime el valor de la temperatura semanal en °C
    print(f'\nEl promedio total de la temperatura semanal es: {promedio_temperatura:.2f} °C')

#Ejecuta la función principal.
temperatura()

print("\n😺¡Buen día!✨")