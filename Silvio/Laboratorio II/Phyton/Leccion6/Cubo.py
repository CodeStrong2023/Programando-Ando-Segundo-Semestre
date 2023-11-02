class Prisma:
    """
    Clase para crear y calcular volumen de un prisma rectangular
    """

    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundidad

# Solicitar al usuario que introduzca las dimensiones del prisma
ancho = float(input("Introduce el ancho del prisma: "))
alto = float(input("Introduce el alto del prisma: "))
profundidad = float(input("Introduce la profundidad del prisma: "))
prisma = Prisma(ancho, alto, profundidad)

# Calcular y mostrar el volumen del prisma
print(f"El volumen del prisma es: {prisma.calcular_volumen()}")
