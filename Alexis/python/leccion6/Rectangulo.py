class Rectangulo:
    """
    crear una clase llamada rectangulo, debe tener 2 atributos: altura y bas
    el nombre del metodo sera calcular el areautilizando la formula:
    area = base * altura. pero la base y la altura deben ser ingresados por
    el usuario y los objetos deben ser tres
    """
    def __int__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return self.base * self.altura

base = int(input("digite el numero para la base del rectangulo: "))
altura = int(input("digite el numero para la altura del rectangulo: "))
rectangulo1 = Rectangulo(base, altura)
print(f"el area del rectangulo es: {rectangulo1.calcular_area()}")


