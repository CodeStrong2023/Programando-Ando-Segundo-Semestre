class Cubo:
    """
    Crear la clase Cubo con los atributos alto ancho y profundidad con un metodo
    calcular_volumen que tendra la formula:
    volumen = ancho * altura * profundidad
    que el usuario ingrese los valores
    """
    def __init__(self, ancho, altura, profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profundidad = profundidad
    def calcular_volumen(self):
        return self.altura*self.ancho*self.profundidad
ancho = int(input("Digite el ancho del cubo\n"))
altura = int(input("Digite la altura del cubo\n"))
profundidad = int(input("Digite la profundidad del cubo\n"))
cubo = Cubo(ancho, altura, profundidad)
print(f'El volumen del cubo es {cubo.calcular_volumen()}')
