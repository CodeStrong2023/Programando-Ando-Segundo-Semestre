class Rectangulo:
    """
    Ejercicio RECTANGULO:
    Crear una clase llamada REctangulo, debe tener 2 atributos: altura y base
    el nombre del metodo sera calcular area utiolizando la formula:
    area = base*altura. PEro la base y la altura deben ser ingresadar por
    el usuario y los objetos deben ser tres.
    """
    def __init__(self, altura, base):#crear metodo inicializador
        self.altura = altura#inicializar atributos
        self.base = base

    def calcular_base(self):#creamos el metodo calculador que retorna el area
        return self.base * self.altura

base = int(input('Digite el numero para la base del rectangulo: '))#pedimos los datos al usuario
altura = int(input('Digite el numero para la altura del rectangulo: '))

rectangulo1 = Rectangulo(base,altura)#asignamos a un objeto en base a al constructor Rectangulo los argumentos
print(f'El area del rectangulo es: {rectangulo1.calcular_base()}')