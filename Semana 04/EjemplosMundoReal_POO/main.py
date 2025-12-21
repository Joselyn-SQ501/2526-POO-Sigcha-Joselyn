# Este programa desarrolla un ejemplo del mundo real utilizando Programación Orientada a Objetos (POO), modelando un sistema de
# gestión gatuna. El sistema permite administrar información relacionada con los datos generales del gato, su dieta,
# entretenimiento y rutina diaria, mediante el uso de clases con atributos y métodos claramente definidos, demostrando la
# interacción entre objetos.

#Importa las clases existentes en el programa
from datos_gatos import datos_gatos
from dieta_gatos import dieta_gatos
from entretenimiento_gatos import entretenimiento_gatos
from rutina_gato import rutina_gato

#Clase principal del programa.
class main:
    print("Bienvenido al sistema de gestión de gatuna 😺\n")

    # Instancia de la gestión de datos del gato
    datos = datos_gatos()

    print("Datos del michi 😺")

    datos.datos_pedidos() # Llama al método de pedir datos de la instancia datos
    datos.mostrar_datos() # Llama al método mostrar datos de la instancia datos
    datos.validar_datos()  # Llama al método validar datos de la instancia datos

    # Instancia de la gestión de la dieta del gato
    dieta = dieta_gatos()
    print(f"\n🍗Ahora, especifica la dieta de {datos.nombre} 😺 por favor")
    dieta.dieta_dia(datos.nombre)   # Llama al método de dieta del día de la instancia dieta
    dieta.mostrar_dieta() # Llama al método de mostrar dieta de la instancia dieta
    dieta.validar_dieta_seleccionada(datos.nombre) # Llama al método de validar dieta de la instancia dieta

    # Instancia de la gestión de la rutina del gato
    rutina = rutina_gato()
    print(f"\n💤Ahora, define la rutina de {datos.nombre} 😺")
    rutina.definir_rutina(datos.nombre) # Llama al método definir rutina de la instancia rutina
    rutina.mostrar_rutina() # Llama al método de mostrar rutina de la instancia rutina
    rutina.validar_rutina_definida(datos.nombre) # Llama al método de validar rutina de la instancia rutina

    # Instancia de la gestión del entretenimiento del gato
    entretenimiento = entretenimiento_gatos()
    print(f"\n🎣Finalmente, ingresa las actividades de entretenimiento de {datos.nombre} 😺")
    entretenimiento.seleccionar_entretenimiento(datos.nombre) # Llama al método seleccionar entretenimiento de la instancia entretenimiento
    entretenimiento.mostrar_entretenimiento() # Llama al método de mostrar entretenimiento de la instancia entretenimiento
    entretenimiento.validar_entretenimiento_seleccionado(datos.nombre) # Llama al método validar entretenimiento de la instancia entretenimiento

    print("\n¡Gracias por usar el sistema de gestión de gatos!😺¡Buen día!✨")