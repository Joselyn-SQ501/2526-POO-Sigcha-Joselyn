
print("\n📝Ejemplos de Técnicas de POO con GATITOS 😺")
print("Abstracción, Encapsulación, Herencia y Polimorfismo")

# ------------------------------
# ABSTRACCIÓN: clase base Gato
# ------------------------------
class Gato:
    """
    ABSTRACCIÓN:
    Esta clase representa la idea general de un gato.
    No define un tipo específico de gato, sino una base común
    con las características y acciones básicas que todos los
    gatos pueden tener: nombre, edad y la capacidad de maullar.
    Esto es ABSTRACCIÓN: quedarse solo con lo esencial del objeto.
    """
    #Constructor de la clase gato
    def __init__(self, nombre, edad):
        #Atributos básicos comunes de cualquier gato
        self.nombre = nombre
        self.edad = edad
    #Imprime la información de los atributos del gato
    def describir(self):
        #Imprime la información de los atributos del gato
        print(f"Soy {self.nombre} y tengo {self.edad} años gatunos.")

    def maullar(self):
        #Método general que se especializará en las subclases (polimorfismo)
        print("Miau Miau Miau.")


# -----------------------------------
# ENCAPSULACIÓN: energía del gato
# -----------------------------------
class GatoEnergia(Gato):
    """
    ENCAPSULACIÓN:
    El atributo energía es privado (no se accede directamente).
    Solo se puede consultar o modificar usando métodos.
    """

    def __init__(self, nombre, edad, energia_inicial=100):
        super().__init__(nombre, edad)
        #Atributo privado (no se modifica directamente)
        self.__energia = energia_inicial

    def obtener_energia(self):
        #Getter que devuelve el valor actual de la energía.
        return self.__energia

    def jugar_fuerte(self, minutos):
        #Disminute la energía según el tiempo de juego en minutos
        gasto = minutos * 2
        self.__energia = max(0, self.__energia - gasto)
        #Imprime el nivel de energía del gato tras el juego
        print(f"{self.nombre} ha jugado {minutos} minutos. Energía ahora: {self.__energia}")

    def ir_a_descasar(self):
        #Aumenta la energía según el tiempo de descanso sin pasar de 100
        self.__energia = min(100, self.__energia + 30)
        #Imprime el nivel de energía del gato tras el descanso
        print(f"{self.nombre} fue a descansar. Energía ahora: {self.__energia}")


# ------------------------------
# HERENCIA: distintos tipos de gatos
# ------------------------------
class GatoDomestico(GatoEnergia):
    """
    HERENCIA:
    GatoDomestico hereda atributos y métodos de GatoEnergia (y a su vez de Gato).
    Añade un nuevo atributo (color) y un nuevo método (ronronear).
    """

    def __init__(self, nombre, edad, energia_inicial=100, color="gris"):
        super().__init__(nombre, edad, energia_inicial)
        self.color = color

    def ronroneo_amigable(self):
        #Acción exclusiva de los gatos domésticos en ambientes tranquilos
        print(f"{self.nombre} ronronea suavemente... prrrrr 😺")

    # POLIMORFISMO: redefinición de maullar()
    def maullar(self):
        #Imprime el maullido más característico de gatos domésticos en ambientes tranquilos.
        print(f"{self.nombre} dice: miau miau tranquilo (gato doméstico).")


class GatoCallejero(GatoEnergia):
    """
    HERENCIA:
    GatoCallejero también hereda de atributos y métodos de GatoEnergia.
    Tiene habilidades diferentes para sobrevivir en la calle.
    """

    def __init__(self, nombre, edad, energia_inicial=80, barrio="Centro"):
        super().__init__(nombre, edad, energia_inicial)
        self.barrio = barrio

    def pelear(self, otro_gato):
        #Imprime la situación de una pelea entre dos gatos, dónde ambos pierden energía.
        print(f"{self.nombre} se pelea con {otro_gato.nombre} en el barrio {self.barrio}.")
        self.jugar_fuerte(10)
        otro_gato.jugar_fuerte(10)

    # POLIMORFISMO: maulla distinto al doméstico y a veces bufa
    def maullar(self):
        #Imprime el maullido característico de gatos callejeros por el entorno hostil en el que se encuentran
        print(f"{self.nombre} dice: MIAUUU fuerte y bufa (gato callejero).")


# --------------------------------
# POLIMORFISMO en acción
# --------------------------------
def concierto_de_maullidos(lista_gatos):
    """
    POLIMORFISMO:
    Esta función recibe una lista de gatos de distintos tipos.
    Llama al mismo método maullar(), pero cada gato responde
    de forma diferente según su clase.
    """
    print("Concierto de maullidos (Polimorfismo)")
    for gato in lista_gatos:
        #Aquí está el polimorfismo por el mismo mensaje y distinta respuesta
        gato.maullar()


# ------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------
if __name__ == "__main__":
    # Crear gatitos
    gato1 = GatoDomestico("Mi Hen", 2, color="blanco")
    gato2 = GatoCallejero("Bigotes", 4, barrio="Norte")

    print("----------------------------------------------")
    # IMPRIME EL EJEMPLO DE ABSTRACCIÓN
    print("Descripción de los gatos (Abstracción)")
    gato1.describir()
    gato2.describir()
    print("----------------------------------------------")

    # IMPRIME EL EJEMPLO DE ENCAPSULACIÓN
    print("Energía de los gatos (Encapsulación)")
    print("\nEnergía inicial de", gato1.nombre, ":", gato1.obtener_energia())
    gato1.jugar_fuerte(15)
    gato1.ir_a_descasar()
    print("\nEnergía inicial de", gato2.nombre, ":", gato2.obtener_energia())
    gato2.jugar_fuerte(5)
    print("----------------------------------------------")

    # IMPRIME EL EJEMPLO DE HERENCIA
    print("Comportamientos específicos por Herencia")
    gato1.ronroneo_amigable()
    gato2.pelear(gato1)
    print("----------------------------------------------")

    # IMPRIME EL EJEMPLO DE POLIMORFISMO
    concierto_de_maullidos([gato1, gato2])
    print("----------------------------------------------")

    print("\n😺¡Buen día!✨")