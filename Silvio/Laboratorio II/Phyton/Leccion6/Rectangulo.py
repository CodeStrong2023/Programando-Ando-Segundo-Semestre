class Rectangulo:
    """
    Clase con atributos y metodo para calcular area
    """
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

# Solicitar al usuario que introduzca las dimensiones del rectángulo
largo = float(input("Introduce el largo del rectángulo: "))
ancho = float(input("Introduce el ancho del rectángulo: "))
rectangulo = Rectangulo(largo, ancho)

# Calcular y mostrar el área del rectángulo
print(f"El área del rectángulo es: {rectangulo.calcular_area()}")
