class Rectangulo:
    """
    Crear una clase llamada Rectangulo, debe tener 2 atributos: altura y base
    el nombre del metodo sera calcular_area utilizando la formula:
    area = base * altura. Pero la base y la altura deben ser ingresadas por el usuario y los objetos deben ser 3
    """
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base
    def calcular_area(self):
        return self.altura * self.base

print("Primer rectangulo")
base = int(input("Digite el numero para la base del rectangulo\n"))
altura = int(input("Digite el numero para la altura\n"))
rectangulo1 = Rectangulo(base, altura)
print(f'El area del rectangulo es {rectangulo1.calcular_area()}\n')

print("Segundo rectangulo")
base = int(input("Digite el numero para la base del rectangulo\n"))
altura = int(input("Digite el numero para la altura\n"))
rectangulo2 = Rectangulo(base, altura)
print(f'El area del rectangulo es {rectangulo2.calcular_area()}\n')

print("Tercer rectangulo")
base = int(input("Digite el numero para la base del rectangulo\n"))
altura = int(input("Digite el numero para la altura\n"))
rectangulo3 = Rectangulo(base, altura)
print(f'El area del rectangulo es {rectangulo3.calcular_area()}\n')
