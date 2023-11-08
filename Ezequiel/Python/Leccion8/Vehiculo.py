class Vehiculo:
    '''
    Definir una clase  padre llamada Vehiculo y dos clases hijas llamads Auto y Bicicleta, las cuales heredan de la
    clasepadre Vehiculo. La clase padre debe tener los siguientes atribtos y metodos:

    Vehculo (clase padre)
    -Atributos(color, ruedas)
    -Metodos(__init__(color, ruedas) y __str__())

    Auto (clase padre)
    -Atributos(velocidad(km/hr))
    -Metodos(__init__y __str__())

    Vehculo (clase padre)
    -Atributos(tipo(urbana/montania/etc.))
    -Metodos(__init__y __str__())

    Crear un objeto de cada clase
    '''

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return 'Color ' +self.color+ " Ruedas: " + str(self.ruedas)

class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color,ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__() + ', Velocidad(km/hr): ' + str(self.velocidad)

class Bicileta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ', Tipo: ' + str(self.tipo)

# Primer objeto de la clase padre Vehiculo
vehiculo = Vehiculo('Blanco', 4)
print(vehiculo)

# Segundo objeto de la clase Auto
auto = Auto('Blanco', 4, 120)
print(auto)

# Tercer objeto de la clase Bicicleta
bici = Bicileta('Blanco', 4, 'Urbana')
print(bici)